# PawPal+

A Streamlit app for daily pet care task scheduling.

## Overview

- Lets an owner register pets, add care tasks (walks, feeding, meds, etc.), and generate a prioritized daily schedule.
- All task management and scheduling logic is handled by a single `PetCareService` singleton.
- Stack: Python · Streamlit · pytest

---

## Architecture

### Enums

| Enum | Values |
|------|--------|
| `Species` | `CAT`, `DOG`, `OTHER` |
| `Priority` | `HIGH`, `MEDIUM`, `LOW` |
| `Status` | `PENDING`, `COMPLETED`, `SKIPPED` |

### Classes

| Class | Attributes | Key Methods | Role |
|-------|-----------|-------------|------|
| `Preferences` | `reminder_time` | — | Owner-level scheduling settings |
| `Pet` | `name`, `age`, `breed`, `species` | — | Represents a single pet |
| `Owner` | `name`, `preferences`, `pets[]` | `add_pet()` | Links an owner to their pets |
| `Task` | `title`, `duration_minutes`, `priority`, `pet`, `time`, `status` | — | A schedulable pet-care activity |
| `Schedule` | `tasks[]`, `description` | — | Output of the scheduling algorithm |
| `PetCareService` | `tasks[]` (singleton) | `add_task()`, `remove_task()`, `update_task()`, `get_tasks_for_pet()`, `filter_tasks_by_status()`, `filter_tasks_by_priority()`, `generate_schedule()` | Singleton; manages all tasks and produces schedules |

---

## Scheduling Algorithm

`PetCareService.generate_schedule()`:

1. Filters out any tasks with `Status.COMPLETED`.
2. Sorts remaining tasks by priority: `HIGH` → `MEDIUM` → `LOW`.
3. Returns a `Schedule` containing the ordered task list and a summary description string.

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```
## Run the App

```bash
python main.py
```

## Run Tests

```bash
pytest -v
```
or
```bash
python -m pytest 
```

Tests live in `tests/test_pawpal.py` and cover: singleton behavior, task add/remove, priority ordering, completed-task exclusion, and per-pet filtering.
