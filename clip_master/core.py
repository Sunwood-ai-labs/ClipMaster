import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt6.QtGui import QIcon, QMouseEvent
from PyQt6.QtCore import Qt, QTimer, QPoint, QThreadPool, pyqtSlot
import pyperclip
import ctypes

from .gui import setup_ui
from .utils import check_clipboard, add_to_history
from .workers import LLMWorker
from .config import ICON_PATH, INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT, MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT, CLIPBOARD_CHECK_INTERVAL, STYLE_SHEET

class ClipboardViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(100, 100, INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT)

        # Add this line to define the margin attribute
        self.margin = 10  # リサイズ可能な境界の幅

        # アプリケーションアイコンの設定
        icon = QIcon(ICON_PATH)
        self.setWindowIcon(icon)
        
        # タスクバーアイコンの設定（Windows用）
        if os.name == 'nt':
            myappid = 'mycompany.myproduct.subproduct.version'  # 任意の文字列
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        QApplication.setWindowIcon(icon)

        setup_ui(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_clipboard)
        self.timer.start(CLIPBOARD_CHECK_INTERVAL)

        self.last_clipboard = ""
        self.clipboard_history = []

        self.threadpool = QThreadPool()

        self.setStyleSheet(STYLE_SHEET)

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
            self.process_button.setEnabled(False)
            messages = [
                {"role": "user", "content": prompt},
                {"role": "user", "content": content}
            ]
            worker = LLMWorker(messages, model_name)
            worker.signals.finished.connect(self.on_llm_finished)
            worker.signals.error.connect(self.on_llm_error)
            self.threadpool.start(worker)
        else:
            QMessageBox.warning(self, "エラー", "指示プロンプトまたはテキストが空です。")

    def on_llm_finished(self, result):
        self.text_edit.setPlainText(result)
        pyperclip.copy(result)
        self.process_button.setEnabled(True)

    def on_llm_error(self, error):
        QMessageBox.warning(self, "エラー", f"LLMへのリクエスト中にエラーが発生しました:\n{error}")
        self.process_button.setEnabled(True)

    def check_clipboard(self):
        clipboard_content = check_clipboard(self.last_clipboard)
        if clipboard_content:
            self.last_clipboard = clipboard_content
            self.show_clipboard()
            self.show()
            add_to_history(self, clipboard_content)

    def load_from_history(self, item):
        from .utils import load_from_history
        load_from_history(self, item)

    def clear_history(self):
        from .utils import clear_history
        clear_history(self)

    def copy_selected_item(self):
        from .utils import copy_selected_item
        copy_selected_item(self)

    def delete_selected_item(self):
        from .utils import delete_selected_item
        delete_selected_item(self)

    def export_history(self):
        from .utils import export_history
        export_history(self)

    def import_history(self):
        from .utils import import_history
        import_history(self)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            self.mouse_pos = event.globalPosition().toPoint()
            event.accept()
            if self.cursor().shape() != Qt.CursorShape.ArrowCursor:
                self.resizing = True
                self.dragging = False

    def mouseMoveEvent(self, event: QMouseEvent):
        pos = event.globalPosition().toPoint()
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

    def mouseReleaseEvent(self, event: QMouseEvent):
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

        if rect.width() < MIN_WINDOW_WIDTH:
            rect.setWidth(MIN_WINDOW_WIDTH)
        if rect.height() < MIN_WINDOW_HEIGHT:
            rect.setHeight(MIN_WINDOW_HEIGHT)

        self.setGeometry(rect)
