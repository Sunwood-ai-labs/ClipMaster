import sys
import argparse
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from qt_material import apply_stylesheet
from .core import ClipboardViewer
from .config import ICON_PATH

def main():
    parser = argparse.ArgumentParser(description="ClipMaster - A clipboard management tool")
    parser.add_argument("--cli", action="store_true", help="Launch the GUI version")
    args = parser.parse_args()

    if args.cli:
        print("CLI version not implemented yet. Use --gui to launch the GUI version.")
        return 1
    else:
        app = QApplication(sys.argv)
        apply_stylesheet(app, theme='dark_purple.xml')
        icon = QIcon(ICON_PATH)
        app.setWindowIcon(icon)
        viewer = ClipboardViewer()
        viewer.show()
        return app.exec()
        
if __name__ == "__main__":
    sys.exit(main())
