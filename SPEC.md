# ScreenshotChecker Software Requirements Specification

Version: 1.0
Status: Draft

---

# 1. Purpose

ScreenshotChecker is a desktop application for macOS that monitors graphical user interfaces by comparing consecutive screenshots.

The application periodically captures screenshots, compares user-defined rectangular regions, and reports whether each region behaves as expected.

The application is intended for GUI monitoring, diagnostics and regression testing.

---

# 2. Design Goals

The application shall:

- produce deterministic results;
- minimize false alarms;
- remain responsive during monitoring;
- support up to 250 monitored regions;
- provide useful diagnostics;
- separate GUI and comparison logic.

---

# 3. Definitions

Screenshot

Complete image captured from one monitor.

Region

Rectangular area inside a screenshot.

Previous screenshot

The screenshot captured immediately before the current screenshot.

Current screenshot

The newest captured screenshot.

Detected change

Boolean result produced by the comparison algorithm.

Expected change

Boolean value configured by the user.

Result

OK if

    detected_change == expect_change

otherwise BAD.

---

# 4. Functional Requirements

## FR-001 Screenshot Capture

The application shall capture screenshots of one selected monitor.

---

## FR-002 Region Selection

The user shall be able to define up to 250 rectangular regions.

---

## FR-003 Region Model

Each region shall contain:

- id
- name
- x
- y
- width
- height
- expect_change
- comparison settings
- enabled

---

## FR-004 Monitoring

Monitoring sequence:

1. capture screenshot
2. wait configured interval
3. capture next screenshot
4. compare all enabled regions
5. report OK/BAD
6. repeat until stopped

---

## FR-005 Region Evaluation

Each region shall be evaluated independently.

Evaluation rule:

region_ok = (detected_change == expect_change)

---

## FR-006 Comparison Methods

Supported methods:

- exact
- pixel_threshold
- ssim (optional)

---

## FR-007 Results

The application shall report:

- OK
- BAD

Results shall be visible in the GUI and written to logs.

---

# 5. Diagnostics

For every comparison record:

- timestamp
- region id
- region name
- comparison method
- expected change
- detected change
- status
- changed pixel count
- total pixel count
- changed pixel ratio

For BAD results the application may save diagnostic images.

---

# 6. Configuration

Configuration shall be stored in JSON.

Configuration shall include:

- schema version
- selected monitor
- monitoring interval
- region list

Configuration shall be validated before use.

---

# 7. GUI

The GUI shall provide:

- monitor selection
- screenshot preview
- rectangle selection
- region editing
- monitoring controls
- result table
- configuration save/load
- clear error reporting

The GUI shall remain responsive during monitoring.

---

# 8. Platform

Target platform:

macOS Sequoia 15.7.3

Support:

- Retina displays
- multiple monitors
- Screen Recording permission

---

# 9. Acceptance Criteria

A milestone is complete only when:

- application starts
- feature works
- manual tests pass
- automated tests pass