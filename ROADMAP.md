# ScreenshotChecker Roadmap

Version: 1.0

This document describes the planned evolution of ScreenshotChecker.

Only features that provide clear value should be implemented.

A roadmap item may change as development progresses.

---

# Guiding Principles

- Always keep the application usable.
- Every released version must be stable.
- New features must not reduce reliability.
- Simplicity is preferred over feature count.
- Deterministic behaviour is preferred over AI or heuristics.
- Performance optimization should follow profiling.

---

# Version 1.0
## Goal

Reliable screenshot comparison.

## Features

- monitor selection
- screenshot capture
- rectangular region selection
- up to 250 regions
- region names
- expected change flag
- exact comparison
- threshold comparison
- optional SSIM
- monitoring loop
- JSON configuration
- logging
- diagnostic images
- unit tests
- macOS application packaging

Status

Current development target.

---

# Version 1.1
## Goal

Better usability.

## Planned Features

- region duplication
- region enable/disable
- reorder regions
- zoomable screenshot viewer
- keyboard shortcuts
- improved status bar
- comparison progress indicator
- configurable colors
- dark mode support
- recent configuration list

Priority

High

---

# Version 1.2
## Goal

Improve diagnostics.

## Planned Features

- side-by-side comparison viewer
- overlay mode
- blinking difference viewer
- heat map visualization
- comparison statistics
- session summary
- HTML report generation
- CSV export
- PDF report generation

Priority

High

---

# Version 1.3
## Goal

Advanced comparison.

## Planned Features

- ignore selected subregions
- comparison masks
- multiple comparison profiles
- adaptive thresholds
- optional Gaussian blur
- optional morphology filtering
- color-only comparison
- grayscale comparison
- edge comparison

Priority

Medium

---

# Version 1.4
## Goal

Automation.

## Planned Features

- automatic configuration loading
- command-line interface
- scheduled monitoring
- configuration templates
- profile switching
- automatic result archive
- batch comparison mode

Priority

Medium

---

# Version 1.5
## Goal

Workflow improvements.

## Planned Features

- project files
- multiple monitor configurations
- configuration import/export
- favorites
- session history
- comparison history
- undo/redo

Priority

Medium

---

# Version 2.0
## Goal

Professional GUI testing tool.

## Planned Features

- baseline image management
- multiple baselines
- baseline approval workflow
- image version history
- comparison history browser
- configurable pass/fail rules
- project statistics
- plugin architecture

Priority

Future

---

# Version 2.1
## Goal

Better comparison algorithms.

## Planned Features

- template matching
- feature matching
- OCR support
- object detection
- text comparison
- histogram comparison
- perceptual hashing

Priority

Future

---

# Version 2.2
## Goal

Recording.

## Planned Features

- screenshot recording
- time-lapse playback
- animated GIF export
- MP4 export
- event timeline

Priority

Future

---

# Version 3.0
## Goal

Testing framework.

## Planned Features

- record user actions
- replay mouse actions
- replay keyboard actions
- automatic screenshot checkpoints
- scripted test execution
- project runner
- regression test suites

Priority

Long-term

---

# Version 3.1
## Goal

External integrations.

## Planned Features

- REST API
- Python API
- plugin SDK
- GitHub Actions support
- Jenkins integration
- GitLab CI integration

Priority

Long-term

---

# Version 4.0
## Goal

AI-assisted diagnostics.

## Planned Features

- natural-language explanation of changes
- automatic change classification
- false-positive suggestions
- automatic threshold recommendation
- comparison parameter optimization

Priority

Research

---

# Candidate Features

These ideas have not yet been accepted into the roadmap.

- OCR-based region validation
- image annotation tools
- screen recording
- multi-user projects
- cloud synchronization
- remote monitoring
- email notifications
- Slack notifications
- Teams notifications
- Telegram notifications
- live dashboard
- embedded scripting
- Lua plugins
- Python plugins
- comparison macros
- database backend

---

# Explicit Non-Goals

The first versions of ScreenshotChecker are not intended to become:

- a Selenium replacement
- a web browser testing framework
- a cloud service
- a machine learning project
- a distributed monitoring platform
- a general image editor

---

# Release Policy

A new version should be released only when:

- all planned features are implemented;
- manual tests pass;
- automated tests pass;
- documentation is updated;
- no known critical bugs remain.