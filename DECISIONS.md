# ScreenshotChecker Design Decisions

Version: 1.0

---

## DD-001

Language

Python

Reason

Rapid development, excellent ecosystem.

---

## DD-002

GUI

PySide6

Reason

Stable Qt framework with QRubberBand support.

---

## DD-003

Screenshot Capture

MSS

Reason

Simple, reliable and cross-platform.

---

## DD-004

Image Processing

NumPy

Reason

Efficient array operations.

---

## DD-005

Comparison

OpenCV absdiff

Reason

Deterministic, configurable and fast.

---

## DD-006

Exact Comparison

NumPy array equality

Reason

Useful for diagnostics.

---

## DD-007

Optional Comparison

SSIM

Reason

Available for future advanced comparison.

---

## DD-008

Configuration

JSON

Reason

Human-readable and versionable.

---

## DD-009

Monitoring

QTimer

Reason

Non-blocking Qt event loop.

---

## DD-010

Evaluation Rule

region_ok = (detected_change == expect_change)

Reason

Simple deterministic logic.

---

## DD-011

GUI Labels

Must change

Must remain unchanged

Reason

Clearer than numeric flags.

---

## DD-012

Testing

pytest

Reason

Standard Python testing framework.

---

## DD-013

Packaging

PyInstaller

Reason

Native macOS .app generation.