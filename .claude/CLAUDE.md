# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**PawPal+** is an AI110 Module 2 assignment — a Streamlit app for daily pet care task scheduling. The backend logic lives in `pawpal_system.py`; the UI skeleton is in `app.py`.

## Commands

```bash
# Setup
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run app
streamlit run app.py

# Run tests
pytest -v

# Run a single test file
pytest tests/test_scheduler.py -v
```

## Architecture

The system design is defined in `PawpalClassDiagram.mmd` (Mermaid syntax). Key classes:

- **`Preferences`** — owner settings (e.g., reminderTime)
- **`Owner`** — name, preferences, list of pets
- **`Pet`** — name, age, breed, species (enum: Cat/Dog/Other)
- **`Task`** — title, durationMinutes, time, priority (High/Medium/Low), status (Pending/Completed/Skipped), assigned pet
- **`Schedule`** — list of tasks + a description string explaining the plan
- **`PetCareService`** — singleton service; manages tasks and generates schedules via `generateSchedule()`; uses private `isConflict()` internally

**Data flow**: `Owner` owns 1+ `Pet`s → `Task`s are assigned to a `Pet` → `PetCareService` takes tasks and produces a `Schedule`.

All backend logic belongs in `pawpal_system.py`. Once implemented, `app.py` imports from it and calls `PetCareService` to build and display the schedule.

## Integration Pattern

```python
# app.py — expected wiring once backend exists
from pawpal_system import Owner, Pet, Task, PetCareService, Species, Priority

service = PetCareService.get_instance()
owner = Owner(name=owner_name, preferences=..., pets=[pet])
task = Task(title="Morning walk", duration_minutes=20, priority=Priority.HIGH, pet=pet)
service.add_task(task)
schedule = service.generate_schedule()
st.write(schedule.description)
```

## Design Notes

- `PetCareService` is a **singleton** — only one instance manages all state.
- `isConflict(task1, task2)` is private; it checks for overlapping times and is called internally by `generateSchedule`.
- Scheduling algorithm baseline: sort tasks by priority, fit within available time, skip what doesn't fit.
- Hard constraints (time conflicts) vs. soft constraints (preferences) should be documented in `reflection.md`.
- Tests go in `test_*.py` files at the project root or in a `tests/` directory.
