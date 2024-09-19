import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QTextEdit, QLabel, QFrame, QListWidget, QSplitter, QMessageBox, QLineEdit)
from PyQt6.QtGui import QIcon, QFont, QMouseEvent, QCursor
from PyQt6.QtCore import Qt, QTimer, QPoint, QRect, QSize, QRunnable, QThreadPool, pyqtSlot, pyqtSignal, QObject
import pyperclip
import litellm  # litellmをインポート
from qt_material import apply_stylesheet

class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(40)  # タイトルバーの高さを固定
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.icon_label = QLabel()
        self.icon_label.setPixmap(QIcon("icon2.png").pixmap(20, 20))
        self.icon_label.setStyleSheet("padding: 5px;")
        self.layout.addWidget(self.icon_label)

        self.title = QLabel("ClipMaster")  # アプリ名を変更
        self.title.setStyleSheet("font-size: 14px; font-weight: bold; padding: 5px;")
        self.layout.addWidget(self.title)

        self.layout.addStretch(1)

        self.minimize_button = QPushButton("－")
        self.minimize_button.clicked.connect(self.window().showMinimized)
        self.layout.addWidget(self.minimize_button)

        self.close_button = QPushButton("✕")
        self.close_button.clicked.connect(self.window().close)
        self.layout.addWidget(self.close_button)

        self.setStyleSheet("""
            QPushButton {
                border: none;
                padding: 5px 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #44475a;
            }
        """)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.window().drag_position = event.globalPosition().toPoint() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.window().move(event.globalPosition().toPoint() - self.window().drag_position)
            event.accept()

class LLMWorkerSignals(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

class LLMWorker(QRunnable):
    def __init__(self, messages, model):
        super().__init__()
        self.messages = messages
        self.model = model
        self.signals = LLMWorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            response = litellm.completion(
                model=self.model,
                messages=self.messages
            )
            print("-------------------")
            print(response.choices[0].message.content)
            if response:
                llm_output = response.choices[0].message.content
                self.signals.finished.emit(llm_output)
            else:
                self.signals.error.emit("LLMからの応答がありません。")
        except Exception as e:
            self.signals.error.emit(str(e))

class ClipboardViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(100, 100, 600, 650)  # ウィンドウ高さを拡大

        # リサイズに関する初期化
        self.resizing = False
        self.dragging = False
        self.drag_position = QPoint()
        self.mouse_pos = None
        self.margin = 10  # リサイズ可能な境界の幅

        # アプリケーションアイコンの設定
        icon_path = os.path.abspath("icon2.png")
        self.setWindowIcon(QIcon(icon_path))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.frame = QFrame()
        self.frame.setObjectName("mainFrame")
        self.frame_layout = QVBoxLayout(self.frame)
        self.frame_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_layout.setSpacing(0)

        self.title_bar = TitleBar(self)
        self.frame_layout.addWidget(self.title_bar, 0)  # サイズポリシーを設定

        # メインコンテンツとサイドバーを分割するスプリッターを追加
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setStyleSheet("QSplitter::handle { background-color: #44475a; }")

        # サイドバー（クリップボード履歴表示用）
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(10, 10, 10, 10)
        self.sidebar_layout.setSpacing(5)

        self.history_label = QLabel("クリップボード履歴")
        self.history_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.sidebar_layout.addWidget(self.history_label)

        self.history_list = QListWidget()
        self.history_list.itemClicked.connect(self.load_from_history)
        self.sidebar_layout.addWidget(self.history_list)

        # ボタンを追加
        self.copy_selected_button = QPushButton("選択項目をコピー")
        self.copy_selected_button.clicked.connect(self.copy_selected_item)
        self.sidebar_layout.addWidget(self.copy_selected_button)

        self.delete_selected_button = QPushButton("選択項目を削除")
        self.delete_selected_button.clicked.connect(self.delete_selected_item)
        self.sidebar_layout.addWidget(self.delete_selected_button)

        self.export_history_button = QPushButton("履歴をエクスポート")
        self.export_history_button.clicked.connect(self.export_history)
        self.sidebar_layout.addWidget(self.export_history_button)

        self.import_history_button = QPushButton("履歴をインポート")
        self.import_history_button.clicked.connect(self.import_history)
        self.sidebar_layout.addWidget(self.import_history_button)

        self.clear_history_button = QPushButton("履歴をクリア")
        self.clear_history_button.clicked.connect(self.clear_history)
        self.sidebar_layout.addWidget(self.clear_history_button)

        self.sidebar.setMinimumWidth(200)
        self.splitter.addWidget(self.sidebar)

        # メインコンテンツ
        self.content = QWidget()
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setSpacing(10)

        # モデル名の入力フィールドを追加
        self.model_label = QLabel("モデル名")
        self.model_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.content_layout.addWidget(self.model_label)

        self.model_input = QLineEdit()
        # self.model_input.setText("bedrock/anthropic.claude-3-sonnet-20240229-v1:0")  # デフォルト値を設定
        self.model_input.setText("claude-3-5-sonnet-20240620")  # デフォルト値を設定
        
        self.content_layout.addWidget(self.model_input)

        # 指示プロンプトのテキストエディットを追加
        self.prompt_label = QLabel("指示プロンプト")
        self.prompt_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.content_layout.addWidget(self.prompt_label)

        self.prompt_edit = QTextEdit()
        self.prompt_edit.setStyleSheet("font-size: 14px;")
        self.prompt_edit.setFixedHeight(100)  # 高さを固定
        self.content_layout.addWidget(self.prompt_edit)

        # テキストエディット
        self.text_label = QLabel("テキスト内容")
        self.text_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.content_layout.addWidget(self.text_label)

        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("font-size: 14px;")
        self.content_layout.addWidget(self.text_edit)

        button_layout = QHBoxLayout()
        self.show_button = QPushButton("クリップボードの内容を表示")
        self.show_button.clicked.connect(self.show_clipboard)
        button_layout.addWidget(self.show_button)

        self.copy_button = QPushButton("テキストをクリップボードにコピー")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(self.copy_button)

        # LLMで処理するボタンを追加
        self.process_button = QPushButton("LLMで処理")
        self.process_button.clicked.connect(self.process_with_llm)
        button_layout.addWidget(self.process_button)

        self.content_layout.addLayout(button_layout)

        self.splitter.addWidget(self.content)
        self.frame_layout.addWidget(self.splitter)
        self.layout.addWidget(self.frame)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_clipboard)
        self.timer.start(1000)

        self.last_clipboard = ""
        self.clipboard_history = []

        self.threadpool = QThreadPool()  # スレッドプールを初期化

        self.setStyleSheet("""
            #mainFrame {
                background-color: #282a36;
                border-radius: 0px;
            }
            QLabel {
                color: #f8f8f2;
            }
            QTextEdit, QPushButton, QListWidget, QLineEdit {
                border-radius: 5px;
            }
            QListWidget {
                background-color: #44475a;
                color: #f8f8f2;
            }
        """)

    def show_clipboard(self):
        clipboard_content = pyperclip.paste()
        self.text_edit.setPlainText(clipboard_content)

    def copy_to_clipboard(self):
        content = self.text_edit.toPlainText()
        pyperclip.copy(content)

    def process_with_llm(self):
        prompt = self.prompt_edit.toPlainText()
        content = self.text_edit.toPlainText()
        model_name = self.model_input.text().strip()
        if not model_name:
            QMessageBox.warning(self, "エラー", "モデル名を入力してください。")
            return
        if prompt.strip() and content.strip():
            # ボタンを無効化して処理中であることを示す
            self.process_button.setEnabled(False)
            # メッセージリストを作成
            messages = [
                {"role": "user", "content": prompt},
                {"role": "user", "content": content}
            ]
            # LLMWorkerを作成してスレッドプールで実行
            worker = LLMWorker(messages, model_name)
            worker.signals.finished.connect(self.on_llm_finished)
            worker.signals.error.connect(self.on_llm_error)
            self.threadpool.start(worker)
        else:
            QMessageBox.warning(self, "エラー", "指示プロンプトまたはテキストが空です。")

    def on_llm_finished(self, result):
        # テキストエディットを更新
        self.text_edit.setPlainText(result)
        # クリップボードにコピー
        pyperclip.copy(result)
        # ボタンを有効化
        self.process_button.setEnabled(True)

    def on_llm_error(self, error):
        QMessageBox.warning(self, "エラー", f"LLMへのリクエスト中にエラーが発生しました:\n{error}")
        # ボタンを有効化
        self.process_button.setEnabled(True)

    def check_clipboard(self):
        clipboard_content = pyperclip.paste()
        if clipboard_content != self.last_clipboard:
            self.last_clipboard = clipboard_content
            self.show_clipboard()
            self.show()
            self.add_to_history(clipboard_content)

    def add_to_history(self, content):
        if content not in self.clipboard_history:
            self.clipboard_history.insert(0, content)
            self.history_list.insertItem(0, content)

    def load_from_history(self, item):
        self.text_edit.setPlainText(item.text())

    def clear_history(self):
        self.clipboard_history.clear()
        self.history_list.clear()

    def copy_selected_item(self):
        selected_items = self.history_list.selectedItems()
        if selected_items:
            content = selected_items[0].text()
            pyperclip.copy(content)

    def delete_selected_item(self):
        selected_items = self.history_list.selectedItems()
        if selected_items:
            item = selected_items[0]
            row = self.history_list.row(item)
            self.history_list.takeItem(row)
            del self.clipboard_history[row]

    def export_history(self):
        with open("clipboard_history.txt", "w", encoding="utf-8") as f:
            for item in self.clipboard_history:
                f.write(item + "\n")

    def import_history(self):
        if os.path.exists("clipboard_history.txt"):
            with open("clipboard_history.txt", "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
                for line in lines:
                    if line not in self.clipboard_history:
                        self.clipboard_history.append(line)
                        self.history_list.addItem(line)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            self.mouse_pos = event.globalPosition().toPoint()
            event.accept()
            # リサイズ開始
            if self.cursor().shape() != Qt.CursorShape.ArrowCursor:
                self.resizing = True
                self.dragging = False  # リサイズ中はドラッグを無効化

    def mouseMoveEvent(self, event):
        pos = event.globalPosition().toPoint()
        rect = self.geometry()
        if self.resizing:
            delta = pos - self.mouse_pos
            self.resizeWindow(delta)
            self.mouse_pos = pos
            event.accept()
        elif self.dragging:
            self.move(pos - self.drag_position)
            event.accept()
        else:
            self.updateCursorShape(event.globalPosition().toPoint())
            event.accept()

    def mouseReleaseEvent(self, event):
        self.resizing = False
        self.dragging = False
        self.updateCursorShape(event.globalPosition().toPoint())
        event.accept()

    def updateCursorShape(self, global_pos):
        rect = self.geometry()
        x = global_pos.x() - rect.x()
        y = global_pos.y() - rect.y()
        margin = self.margin
        if x < margin and y < margin:
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif x > rect.width() - margin and y > rect.height() - margin:
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif x < margin and y > rect.height() - margin:
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif x > rect.width() - margin and y < margin:
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif x < margin:
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif x > rect.width() - margin:
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif y < margin:
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        elif y > rect.height() - margin:
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

    def resizeWindow(self, delta):
        rect = self.geometry()
        cursor_shape = self.cursor().shape()

        if cursor_shape == Qt.CursorShape.SizeHorCursor:
            if self.mouse_pos.x() < rect.center().x():
                rect.setLeft(rect.left() + delta.x())
            else:
                rect.setRight(rect.right() + delta.x())
        elif cursor_shape == Qt.CursorShape.SizeVerCursor:
            if self.mouse_pos.y() < rect.center().y():
                rect.setTop(rect.top() + delta.y())
            else:
                rect.setBottom(rect.bottom() + delta.y())
        elif cursor_shape == Qt.CursorShape.SizeFDiagCursor:
            if self.mouse_pos.x() < rect.center().x():
                rect.setLeft(rect.left() + delta.x())
                rect.setTop(rect.top() + delta.y())
            else:
                rect.setRight(rect.right() + delta.x())
                rect.setBottom(rect.bottom() + delta.y())
        elif cursor_shape == Qt.CursorShape.SizeBDiagCursor:
            if self.mouse_pos.x() < rect.center().x():
                rect.setLeft(rect.left() + delta.x())
                rect.setBottom(rect.bottom() + delta.y())
            else:
                rect.setRight(rect.right() + delta.x())
                rect.setTop(rect.top() + delta.y())

        min_width = 400  # サイドバーがあるため最小幅を大きく設定
        min_height = 450
        if rect.width() < min_width:
            rect.setWidth(min_width)
        if rect.height() < min_height:
            rect.setHeight(min_height)

        self.setGeometry(rect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_purple.xml')

    # アプリケーションアイコンの設定
    icon_path = os.path.abspath("icon2.png")
    app.setWindowIcon(QIcon(icon_path))

    viewer = ClipboardViewer()
    viewer.show()
    sys.exit(app.exec())
