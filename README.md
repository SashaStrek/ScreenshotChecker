# ScreenshotChecker

ScreenshotChecker is a macOS desktop application that monitors graphical user
interfaces by comparing user-defined regions in consecutive screenshots.

## Target Platform

- macOS Sequoia 15.7.3
- Apple Silicon
- Python
- PySide6

## Development Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements-dev.txt