import os

# アイコンファイルのパス
ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "resources", "icon2.png"))

# デフォルトのLLMモデル
DEFAULT_MODEL = "claude-3-5-sonnet-20240620"

# ウィンドウの初期サイズ
INITIAL_WINDOW_WIDTH = 600
INITIAL_WINDOW_HEIGHT = 650

# 最小ウィンドウサイズ
MIN_WINDOW_WIDTH = 400
MIN_WINDOW_HEIGHT = 450

# サイドバーの最小幅
SIDEBAR_MIN_WIDTH = 200

# クリップボードチェックの間隔（ミリ秒）
CLIPBOARD_CHECK_INTERVAL = 1000

# リサイズ可能な境界の幅
RESIZE_MARGIN = 10

# スタイルシート
STYLE_SHEET = """
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
"""
