# ScreenshotChecker Design

Version: 1.0

---

# Architecture

The application is divided into independent layers.

GUI

↓

Monitoring Engine

↓

Capture

↓

Comparison

↓

Diagnostics

Configuration is shared across modules.

---

# Directory Layout

ScreenshotChecker/

app/
core/
diagnostics/
tests/

---

# Module Responsibilities

app/

User interface only.

core/capture.py

Screenshot acquisition.

core/comparison.py

Image comparison algorithms.

core/monitor_engine.py

Monitoring state machine.

core/models.py

Dataclasses and enums.

core/configuration.py

JSON serialization.

diagnostics/

Logging and diagnostic images.

tests/

Unit tests.

---

# Comparison Pipeline

Capture

↓

Crop

↓

Compare

↓

Detected Change

↓

Evaluate

↓

OK/BAD

↓

Diagnostics

---

# Coordinate System

GUI coordinates are temporary.

Stored coordinates are always screenshot pixel coordinates.

GUI converts coordinates before saving.

Only GUI code uses Qt coordinates.

---

# State Machine

Idle

↓

Configuration

↓

Ready

↓

Monitoring

↓

Stopped

↓

Monitoring

↓

Exit

---

# Error Handling

Recover whenever possible.

Never silently ignore exceptions.

Continue processing remaining regions if one region fails.

Unexpected exceptions are logged.

---

# Performance

Correctness is preferred over optimization.

Expected workload:

- up to 250 regions
- screenshots every few seconds

Optimization should be based on profiling.

---

# Coding Rules

Prefer:

- dataclasses
- enums
- pathlib
- type hints
- composition
- explicit code

Avoid:

- global mutable state
- circular imports
- duplicated logic
- very large source files

Core modules shall not depend on Qt.

Image-processing code shall remain independent from the GUI.