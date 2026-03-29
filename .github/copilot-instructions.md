---
name: PawPal+ Workspace Instructions
description: "AI110 Module 2 project: Streamlit pet care planning app. Use when: designing/implementing scheduling logic, building UI components, writing tests, or debugging the application."
---

# PawPal+ Workspace Instructions

## Project Overview

**PawPal+** is a Streamlit application that helps pet owners plan daily care tasks based on constraints (time, priority, owner preferences). This is an assignment for AI110 Module 2 focused on system design, implementation, and testing.

### Project Structure

```
├── app.py                 # Streamlit UI (skeleton provided, awaits backend integration)
├── requirements.txt       # Dependencies: streamlit, pytest
├── reflection.md          # Design documentation and implementation notes
├── README.md              # Project scenario and requirements
└── __pycache__/          # Python cache (ignore)
```

## Development Workflow

### Phase 1: Design (UML)
1. Identify classes: Task, Pet, Owner, Schedule
2. Define attributes and responsibilities for each class
3. Sketch class relationships and method signatures
4. Document in reflection.md under "System Design"

### Phase 2: Implementation
1. Create Python module(s) for core logic (e.g., `models.py`, `scheduler.py`)
2. Implement classes and scheduling algorithm incrementally
3. Add unit tests in `test_*.py` files as you build
4. Connect backend to Streamlit UI in app.py

### Phase 3: Testing & Refinement
1. Run tests frequently: `pytest` or `pytest -v`
2. Refine UML to match actual implementation
3. Update reflection.md with design decisions and tradeoffs

## Key Design Considerations

### Constraints & Priorities
Your scheduler must consider:
- **Time**: Owner availability, task duration
- **Priority**: Task importance (feeding > enrichment)
- **Preferences**: Owner-specified constraints or soft rules

Decide which constraints are "hard" (must respect) vs "soft" (prefer but can violate).

### Scheduling Algorithm
Keep it simple initially: sort by priority, pack by available time. Iterate based on test failures.
Document your tradeoffs in reflection.md section 2b.

### Class Responsibilities
- **Task**: duration, priority, category, description
- **Pet**: species, name, dietary/behavioral info
- **Owner**: name, availability, preferences
- **Schedule**: organize tasks by time, explain reasoning, handle conflicts

## Commands

| Task | Command |
|------|---------|
| Install dependencies | `pip install -r requirements.txt` |
| Run app | `streamlit run app.py` (from workspace root) |
| Run tests | `pytest` or `pytest -v` |
| Test specific file | `pytest tests/test_scheduler.py -v` |

## Common Issues

**Streamlit "No module named" error**
- Ensure venv is activated: `.venv\Scripts\activate` (Windows)
- Verify all imports in app.py match your module structure
- Test imports in Python REPL first: `python -c "from mymodule import MyClass"`

**Tasks not appearing in Streamlit**
- Check `st.session_state.tasks` is populated before rendering
- Remember app.py is only a UI skeleton—you must implement the backend

**Tests fail with import errors**
- Ensure test files use relative imports from project root
- Example: `from models import Task, Pet, Schedule` (not `from ..models`)

## Reflection Checklist

Before finalizing, complete these sections in reflection.md:
- [ ] 1a: Describe your UML design and classes
- [ ] 1b: List any design changes and their rationale
- [ ] 2a: Explain constraints/priorities your scheduler considers
- [ ] 2b: Describe one tradeoff and justify it

## Integration Points

### Connecting Backend to UI
Once your backend is ready, app.py should:
1. Import your classes: `from scheduler import Scheduler` etc.
2. Create instances from st.text_input / st.selectbox values
3. Call scheduler: `plan = scheduler.generate_daily_plan(...)`
4. Display results: `st.write(plan)`, `st.table(schedule_df)`

### Example Flow
```python
owner = Owner(name=owner_name, available_hours=8)
pet = Pet(name=pet_name, species=species)
scheduler = Scheduler(owner, pet)
tasks = [Task(...), Task(...)]  # from st.session_state.tasks
daily_plan = scheduler.generate_daily_plan(tasks)
st.write(daily_plan.explain())  # or similar method
```

## Testing Strategy

Focus tests on:
1. **Task creation**: attributes set correctly
2. **Scheduling logic**: tasks ordered by priority, fit within time
3. **Edge cases**: no tasks, all high-priority (conflict), insufficient time
4. **Explanation**: plan includes reasoning

Example test structure:
```python
# test_scheduler.py
def test_tasks_sorted_by_priority():
    task_low = Task("play", 30, priority=1)
    task_high = Task("feed", 15, priority=3)
    plan = scheduler.generate_daily_plan([task_low, task_high])
    assert plan.tasks[0] == task_high  # high priority first
```

## Hints & Best Practices

- **Start small**: Implement one class at a time, test it, then integrate.
- **Use pytest for TDD**: Write test first, then implement to pass it.
- **Separate concerns**: Keep Streamlit UI separate from scheduling logic.
- **Document assumptions**: If scheduler assumes 24-hour day, say so in a docstring.
- **Ask clarifying questions**: If requirements are ambiguous, state assumptions in reflection.md.

---

**Last updated**: Module 2 project initialization
