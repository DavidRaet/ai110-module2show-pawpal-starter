import streamlit as st

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# ── Owner & Pet Setup ─────────────────────────────────────────────────────────
st.header("Owner & Pet")

col1, col2 = st.columns(2)
with col1:
    owner_name = st.text_input("Owner name", value="Jordan")
with col2:
    reminder_time = st.time_input("Daily reminder time")  # maps to Preferences.reminderTime

st.markdown("#### Pet Details")
col1, col2, col3, col4 = st.columns(4)
with col1:
    pet_name = st.text_input("Pet name", value="Mochi")
with col2:
    pet_age = st.number_input("Age (years)", min_value=0, max_value=30, value=3)
with col3:
    pet_breed = st.text_input("Breed", value="Shiba Inu")
with col4:
    species = st.selectbox("Species", ["Dog", "Cat", "Other"])

st.divider()

# ── Add Task ──────────────────────────────────────────────────────────────────
st.header("Add Task")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])

if st.button("Add task"):
    st.session_state.tasks.append({
        "title": task_title,
        "duration_minutes": duration,
        "priority": priority,
        "pet": pet_name,
        "status": "Pending",
    })

st.divider()

# ── Task List & Management ────────────────────────────────────────────────────
st.header("Tasks")

if st.session_state.tasks:
    col1, col2 = st.columns(2)
    with col1:
        status_filter = st.selectbox(
            "Filter by status", ["All", "Pending", "Completed", "Skipped"]
        )
    with col2:
        priority_filter = st.selectbox(
            "Filter by priority", ["All", "High", "Medium", "Low"]
        )

    displayed = [
        (i, t) for i, t in enumerate(st.session_state.tasks)
        if (status_filter == "All" or t["status"] == status_filter)
        and (priority_filter == "All" or t["priority"] == priority_filter)
    ]

    if displayed:
        for orig_idx, task in displayed:
            with st.container(border=True):
                col1, col2, col3 = st.columns([4, 1, 1])
                with col1:
                    st.markdown(
                        f"**{task['title']}** — {task['duration_minutes']} min"
                        f" | Priority: **{task['priority']}** | Pet: {task['pet']}"
                    )
                    st.caption(f"Status: {task['status']}")
                with col2:
                    if task["status"] != "Completed":
                        if st.button("Complete", key=f"complete_{orig_idx}"):
                            st.session_state.tasks[orig_idx]["status"] = "Completed"
                            st.rerun()
                with col3:
                    if task["status"] != "Skipped":
                        if st.button("Skip", key=f"skip_{orig_idx}"):
                            st.session_state.tasks[orig_idx]["status"] = "Skipped"
                            st.rerun()
    else:
        st.info("No tasks match the current filters.")
else:
    st.info("No tasks yet. Add one above.")

st.divider()


st.header("Schedule")
st.caption("Generates a priority-ordered plan — completed tasks are excluded.")

if st.button("Generate schedule"):
    pending = [t for t in st.session_state.tasks if t["status"] != "Completed"]
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    sorted_tasks = sorted(pending, key=lambda t: priority_order[t["priority"]])

    if sorted_tasks:
        description = (
            f"Generated schedule with {len(sorted_tasks)} task(s), "
            "ordered by priority (High → Medium → Low)."
        )
        st.success(description)
        for task in sorted_tasks:
            st.markdown(
                f"- **{task['title']}** ({task['duration_minutes']} min)"
                f" — {task['priority']} priority | Status: {task['status']}"
                f" | Pet: {task['pet']}"
            )
    else:
        st.info("All tasks are completed — nothing left to schedule!")
