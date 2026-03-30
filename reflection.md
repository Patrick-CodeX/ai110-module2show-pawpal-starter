# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
- My initial design was a modular system using four core classes: `Owner`, `Pet`, `Task`, and `Scheduler`.
- **Owner:** Acts as the primary manager for multiple pet objects.
- **Pet:** Stores metadata (name, species) and maintains a list of specific tasks.
- **Task:** A data class that stores title, duration, start time, and priority level.
- **Scheduler:** A logic-focused class (service layer) that handles sorting and data processing.

**b. Design changes**
- During implementation, I decided to use Python **Dataclasses** for the `Task` and `Pet` objects instead of standard classes.
- I made this change based on AI feedback to keep the code "Pythonic" and cleaner. It simplified the data management by automatically handling the `__init__` and `__repr__` methods, making it much easier to debug.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**
- My scheduler considers two main constraints: **Chronological Time** and **Conflict Detection**.
- I decided that **Time** was the most important constraint because a pet owner needs a sequential timeline for their day. Priority was used as a visual indicator rather than a hard sorting rule to allow the owner more flexibility in their planning.

**b. Tradeoffs**
- **Tradeoff:** My scheduler only detects conflicts for the *exact same start time*. It does not calculate if the duration of one task overlaps into another (e.g., a 60-minute walk starting at 8:00 and a feeding starting at 8:30).
- **Reasoning:** For a pet care assistant, detecting exact time conflicts is the most common use case. Building a full overlapping-duration algorithm would have added unnecessary complexity for an MVP, while exact-time matching remains highly readable for the user.

---

## 3. AI Collaboration

**a. How you used AI**
- I used AI for brainstorming the initial system architecture and generating the **Mermaid.js UML diagram** to visualize the relationships.
- I also used AI to debug **Streamlit's session state**, which was helpful in ensuring that data persisted in memory even when the user added new pets or refreshed the page.

**b. Judgment and verification**
- At one point, the AI suggested using an SQLite database to store the pet information permanently. I chose not to accept this suggestion.
- **Evaluation:** I verified that using `st.session_state` was a better "CLI-first" approach for a prototype, as it requires zero external setup for the user while still allowing for a modular backend logic.

---

## 4. Testing and Verification

**a. What you tested**
- I used `pytest` to test the `add_task` method to ensure the `Pet` object was correctly storing new data.
- I also tested the **Sorting Logic** in the `Scheduler` to verify that task lists are always returned in chronological order (e.g., 08:00 comes before 15:00).
- These tests were critical to ensure that the core "Brain" of the app worked before connecting it to the UI.

**b. Confidence**
- I am 4/5 confident. The scheduler works perfectly for standard 24-hour time inputs (HH:MM).
- Next, I would test edge cases for **invalid time formats** (e.g., a user typing "morning" instead of "08:00") and implement input validation to prevent the program from crashing.

---

## 5. Reflection

**a. What went well**
- I am most satisfied with the **Modular Architecture**. Having the backend logic in `pawpal_system.py` separate from the Streamlit UI made the project very easy to build and test incrementally.

**b. What you would improve**
- In another iteration, I would implement **Duration Overlap Detection**. This would warn the user if they try to schedule a 2-hour walk and a feeding within the same hour.

**c. Key takeaway**
- My key takeaway is that having a clear **UML design** before writing code makes collaborating with AI much more effective. It allows the AI to provide specific, high-quality code that fits into a pre-defined structure rather than generating fragmented logic.