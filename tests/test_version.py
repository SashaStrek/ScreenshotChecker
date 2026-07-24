"""Tests for ScreenshotChecker version constants."""

from __future__ import annotations

from core.version import (
    APPLICATION_NAME,
    APPLICATION_VERSION,
    CONFIGURATION_SCHEMA_VERSION,
)


def test_application_name() -> None:
    """The application name must remain stable."""

    assert APPLICATION_NAME == "ScreenshotChecker"


def test_application_version_is_not_empty() -> None:
    """The application version must be defined."""

    assert APPLICATION_VERSION


def test_configuration_schema_version_is_positive() -> None:
    """Configuration schema versions must be positive integers."""

    assert isinstance(CONFIGURATION_SCHEMA_VERSION, int)
    assert CONFIGURATION_SCHEMA_VERSION >= 1