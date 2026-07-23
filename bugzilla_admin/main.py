"""Main entry point for Bugzilla Admin Client"""

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from bugzilla_admin.ui.main_window import MainWindow
from bugzilla_admin.config import config_manager
from bugzilla_admin.utils.logger import setup_logging


def setup_application_style(app: QApplication) -> None:
    """Setup application style and fonts"""
    # Set default font
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    # Load stylesheet
    stylesheet_path = Path(__file__).parent / "resources" / "styles" / "light.qss"
    if stylesheet_path.exists():
        with open(stylesheet_path, "r") as f:
            app.setStyleSheet(f.read())


def main() -> None:
    """Main application entry point"""
    # Setup logging
    setup_logging()

    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Bugzilla Admin Client")
    app.setApplicationVersion("0.1.0")
    app.setApplicationDisplayName("Bugzilla Administration Client")

    # Setup style
    setup_application_style(app)

    # Create and show main window
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
