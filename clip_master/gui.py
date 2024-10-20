from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit,
                             QLabel, QFrame, QListWidget, QSplitter, QLineEdit)
from PyQt6.QtGui import QIcon, QMouseEvent
from PyQt6.QtCore import Qt, QPoint
from .config import ICON_PATH, DEFAULT_MODEL, SIDEBAR_MIN_WIDTH, STYLE_SHEET

class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(40)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.icon_label = QLabel()
        self.icon_label.setPixmap(QIcon(ICON_PATH).pixmap(20, 20))
        self.icon_label.setStyleSheet("padding: 5px;")
        self.layout.addWidget(self.icon_label)

        self.title = QLabel("ClipMaster")
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

def setup_ui(window):
    window.central_widget = QWidget()
    window.setCentralWidget(window.central_widget)
    window.layout = QVBoxLayout(window.central_widget)
    window.layout.setContentsMargins(0, 0, 0, 0)
    window.layout.setSpacing(0)

    window.frame = QFrame()
    window.frame.setObjectName("mainFrame")
    window.frame_layout = QVBoxLayout(window.frame)
    window.frame_layout.setContentsMargins(0, 0, 0, 0)
    window.frame_layout.setSpacing(0)

    window.title_bar = TitleBar(window)
    window.frame_layout.addWidget(window.title_bar, 0)

    window.splitter = QSplitter(Qt.Orientation.Horizontal)
    window.splitter.setHandleWidth(1)
    window.splitter.setStyleSheet("QSplitter::handle { background-color: #44475a; }")

    # サイドバー
    window.sidebar = QWidget()
    window.sidebar_layout = QVBoxLayout(window.sidebar)
    window.sidebar_layout.setContentsMargins(10, 10, 10, 10)
    window.sidebar_layout.setSpacing(5)

    window.history_label = QLabel("クリップボード履歴")
    window.history_label.setStyleSheet("font-size: 14px; font-weight: bold;")
    window.sidebar_layout.addWidget(window.history_label)

    window.history_list = QListWidget()
    window.history_list.itemClicked.connect(window.load_from_history)
    window.sidebar_layout.addWidget(window.history_list)

    window.copy_selected_button = QPushButton("選択項目をコピー")
    window.copy_selected_button.clicked.connect(window.copy_selected_item)
    window.sidebar_layout.addWidget(window.copy_selected_button)

    window.delete_selected_button = QPushButton("選択項目を削除")
    window.delete_selected_button.clicked.connect(window.delete_selected_item)
    window.sidebar_layout.addWidget(window.delete_selected_button)

    window.export_history_button = QPushButton("履歴をエクスポート")
    window.export_history_button.clicked.connect(window.export_history)
    window.sidebar_layout.addWidget(window.export_history_button)

    window.import_history_button = QPushButton("履歴をインポート")
    window.import_history_button.clicked.connect(window.import_history)
    window.sidebar_layout.addWidget(window.import_history_button)

    window.clear_history_button = QPushButton("履歴をクリア")
    window.clear_history_button.clicked.connect(window.clear_history)
    window.sidebar_layout.addWidget(window.clear_history_button)

    window.sidebar.setMinimumWidth(SIDEBAR_MIN_WIDTH)
    window.splitter.addWidget(window.sidebar)

    # メインコンテンツ
    window.content = QWidget()
    window.content_layout = QVBoxLayout(window.content)
    window.content_layout.setContentsMargins(20, 20, 20, 20)
    window.content_layout.setSpacing(10)

    window.model_label = QLabel("モデル名")
    window.model_label.setStyleSheet("font-size: 14px; font-weight: bold;")
    window.content_layout.addWidget(window.model_label)

    window.model_input = QLineEdit()
    window.model_input.setText(DEFAULT_MODEL)
    window.content_layout.addWidget(window.model_input)

    window.prompt_label = QLabel("指示プロンプト")
    window.prompt_label.setStyleSheet("font-size: 14px; font-weight: bold;")
    window.content_layout.addWidget(window.prompt_label)

    window.prompt_edit = QTextEdit()
    window.prompt_edit.setStyleSheet("font-size: 14px;")
    window.prompt_edit.setFixedHeight(100)
    window.content_layout.addWidget(window.prompt_edit)

    window.text_label = QLabel("テキスト内容")
    window.text_label.setStyleSheet("font-size: 14px; font-weight: bold;")
    window.content_layout.addWidget(window.text_label)

    window.text_edit = QTextEdit()
    window.text_edit.setStyleSheet("font-size: 14px;")
    window.content_layout.addWidget(window.text_edit)

    button_layout = QHBoxLayout()
    window.show_button = QPushButton("クリップボードの内容を表示")
    window.show_button.clicked.connect(window.show_clipboard)
    button_layout.addWidget(window.show_button)

    window.copy_button = QPushButton("テキストをクリップボードにコピー")
    window.copy_button.clicked.connect(window.copy_to_clipboard)
    button_layout.addWidget(window.copy_button)

    window.process_button = QPushButton("LLMで処理")
    window.process_button.clicked.connect(window.process_with_llm)
    button_layout.addWidget(window.process_button)

    window.content_layout.addLayout(button_layout)

    window.splitter.addWidget(window.content)
    window.frame_layout.addWidget(window.splitter)
    window.layout.addWidget(window.frame)

    window.setStyleSheet(STYLE_SHEET)
