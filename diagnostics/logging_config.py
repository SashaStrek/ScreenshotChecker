"""Logging configuration for ScreenshotChecker."""

from __future__ import annotations

import logging
from pathlib import Path


def configure_logging(log_directory: Path | None = None) -> Path:
    """Configure console and file logging.

    Args:
        log_directory:
            Directory in which the application log is created.
            If omitted, a ``logs`` directory is created in the current
            working directory.

    Returns:
        Path to the active log file.
    """

    resolved_log_directory = (
        log_directory if log_directory is not None else Path.cwd() / "logs"
    )
    resolved_log_directory.mkdir(parents=True, exist_ok=True)

    log_file = resolved_log_directory / "screenshotchecker.log"

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    if root_logger.handlers:
        root_logger.handlers.clear()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        filename=log_file,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    return log_file