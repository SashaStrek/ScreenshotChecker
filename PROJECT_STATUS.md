# ScreenshotChecker Project Status

Version: 1.1

---

Current milestone

2 - Screenshot Capture

---

## Milestones

### 0 Planning

Status

✅ Complete

Tasks

* requirements collected
* architecture defined
* documentation created

---

### 1 Environment

Status

✅ Complete

Completed

2026-07-24

Deliverables

* project structure created
* Python 3.12 virtual environment created
* runtime dependencies installed
* development dependencies installed
* minimal PySide6 application created
* logging configuration created
* initial core version module created
* first pytest tests created

Verification

* application starts successfully
* main window opens with the title `ScreenshotChecker`
* main window displays `ScreenshotChecker environment is ready.`
* closing the window terminates the process normally
* application exits with code 0
* log file is created at `logs/screenshotchecker.log`
* application start and stop events are logged
* pytest passes: 4 tests
* Ruff passes
* mypy passes for `core` and `diagnostics`

Environment

* platform: macOS
* architecture: Apple Silicon
* Python: 3.12.13
* pytest: 9.1.1
* pytest-cov: 7.1.0

---

### 2 Screenshot Capture

Status

🟨 In Progress

Goal

Implement screenshot acquisition for one selected monitor.

Deliverables

* monitor enumeration
* monitor data model
* selected-monitor screenshot capture
* screenshot image conversion
* Retina scaling calculation
* multiple-monitor coordinate handling
* Screen Recording permission error handling
* capture unit tests using synthetic data where possible
* manual capture test on macOS

Planned modules

* `core/capture.py`
* `core/models.py`
* `tests/test_capture.py`

Acceptance criteria

* available monitors can be enumerated
* one monitor can be selected
* a screenshot can be captured from the selected monitor
* captured image dimensions are reported correctly
* monitor coordinates are preserved
* Retina scale factors are calculated from actual dimensions
* Screen Recording permission failure produces a clear error
* core capture code does not depend on Qt
* automated tests pass
* manual capture test passes

---

### 3 Comparison Engine

Status

⬜ Not Started

Deliverables

* exact comparison
* pixel threshold comparison
* unit tests

---

### 4 Region Model

Status

⬜ Not Started

Deliverables

* dataclasses
* enums
* validation

---

### 5 Configuration

Status

⬜ Not Started

Deliverables

* JSON save/load
* schema version
* validation

---

### 6 Screenshot Viewer

Status

⬜ Not Started

Deliverables

* screenshot display
* zoom
* monitor preview

---

### 7 Region Selection

Status

⬜ Not Started

Deliverables

* QRubberBand
* numbering
* editing

---

### 8 Monitoring

Status

⬜ Not Started

Deliverables

* timer
* monitoring loop
* stop/start

---

### 9 Results

Status

⬜ Not Started

Deliverables

* result table
* statistics

---

### 10 Diagnostics

Status

⬜ Not Started

Deliverables

* logs
* diagnostic images

---

### 11 Testing

Status

⬜ Not Started

Deliverables

* full pytest suite

---

### 12 Packaging

Status

⬜ Not Started

Deliverables

* macOS `.app`
* installation instructions

---

## Test Status

Last verified

2026-07-24

Commands

```bash
python -m pytest
python -m ruff check .
python -m mypy core diagnostics
python -m app.main
```

Results

```text
pytest: 4 passed
Ruff: all checks passed
mypy: no issues found
application exit code: 0
```

---

## Known Issues

### KI-001 Duplicate virtual-environment prompt marker

The terminal prompt displays:

```text
((.venv) )
```

instead of:

```text
(.venv)
```

Impact

Cosmetic only. The active Python interpreter is correctly located inside the project virtual environment.

Verified interpreter

```text
/Users/astrek/myPerson/PROJECTS/ScreenshotCheker/.venv/bin/python
```

Resolution

Not required for application development. Shell prompt configuration may be corrected separately.

---

## Open Questions

None
