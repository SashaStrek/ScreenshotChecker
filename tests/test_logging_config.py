"""Tests for logging configuration."""

from __future__ import annotations

from pathlib import Path

from diagnostics.logging_config import configure_logging


def test_configure_logging_creates_log_directory(tmp_path: Path) -> None:
    """Logging configuration must create its output directory."""

    log_directory = tmp_path / "logs"

    log_file = configure_logging(log_directory)

    assert log_directory.is_dir()
    assert log_file == log_directory / "screenshotchecker.log"
    assert log_file.exists()