import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾")

st.title("🐾 PawPal+ Care Assistant")

# --- PHASE 3: SESSION STATE (Application Memory) ---
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Default User")

# --- SIDEBAR: MANAGE PETS ---
with st.sidebar:
    st.header("My Pets")
    new_pet_name = st.text_input("Pet Name")
    new_pet_species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Other"])
    if st.button("Add Pet"):
        if new_pet_name:
            st.session_state.owner.add_pet(Pet(new_pet_name, new_pet_species))
            st.success(f"Added {new_pet_name}!")
        else:
            st.error("Enter a name!")

# --- MAIN UI: SCHEDULING ---
if not st.session_state.owner.pets:
    st.info("👈 Start by adding a pet in the sidebar!")
else:
    pet_names = [p.name for p in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Select Pet to Schedule", pet_names)
    selected_pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet_name)

    st.divider()
    st.subheader(f"Add a Task for {selected_pet_name}")
    
    with st.form("task_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            t_name = st.text_input("Task Name (e.g., Feeding)")
            t_time = st.text_input("Time (24hr format HH:MM)", value="08:00")
        with col2:
            t_duration = st.number_input("Duration (mins)", min_value=5, value=15)
            t_priority = st.select_slider("Priority", options=["low", "medium", "high"])
        
        if st.form_submit_button("Add Task"):
            new_task = Task(t_name, int(t_duration), t_time, t_priority)
            selected_pet.add_task(new_task)
            st.toast("Task added!")

    # --- PHASE 4: ALGORITHMIC DISPLAY ---
    st.divider()
    st.subheader("Today's Optimized Schedule")

    if not selected_pet.tasks:
        st.write("No tasks scheduled yet.")
    else:
        # Use Scheduler algorithms
        sorted_tasks = Scheduler.get_sorted_tasks(selected_pet.tasks)
        conflicts = Scheduler.detect_conflicts(selected_pet.tasks)
        total_mins = Scheduler.calculate_total_time(selected_pet.tasks)

        if conflicts:
            st.warning(f"⚠️ Schedule Conflict: Multiple tasks at {', '.join(conflicts)}")

        for t in sorted_tasks:
            status = "✅" if t.completed else "⏳"
            priority_color = {"high": "red", "medium": "orange", "low": "blue"}[t.priority]
            st.markdown(f"{status} **{t.time}** - {t.title} ({t.duration} mins) | :{priority_color}[Priority: {t.priority}]")

        st.info(f"**Total Care Time:** {total_mins} minutes")

        # --- REASONING (Required for grade) ---
        with st.expander("Why was this schedule built this way?"):
            st.write("""
            1. **Chronological Sorting:** Tasks are ordered by time to provide a clear timeline for the owner.
            2. **Conflict Detection:** The system flags overlapping times to prevent double-booking care.
            3. **Visual Cues:** Priority levels are color-coded so the most urgent tasks stand out.
            """)