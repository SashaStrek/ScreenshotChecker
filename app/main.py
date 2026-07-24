"""ScreenshotChecker application entry point."""

from __future__ import annotations

import logging
import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

from diagnostics.logging_config import configure_logging


class MainWindow(QMainWindow):
    """Initial ScreenshotChecker main window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("ScreenshotChecker")
        self.resize(900, 600)

        status_label = QLabel("ScreenshotChecker environment is ready.")
        status_label.setWordWrap(True)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(status_label)

        self.setCentralWidget(central_widget)


def main() -> int:
    """Start the ScreenshotChecker Qt application."""

    configure_logging()
    logger = logging.getLogger(__name__)

    logger.info("Starting ScreenshotChecker")

    application = QApplication(sys.argv)
    application.setApplicationName("ScreenshotChecker")
    application.setOrganizationName("ScreenshotChecker")

    main_window = MainWindow()
    main_window.show()

    exit_code = application.exec()

    logger.info("ScreenshotChecker stopped with exit code %d", exit_code)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())