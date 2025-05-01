# A Terminal-based habit tracker using python
A simple command-line application built in Python to help track your daily habits. Mark them as completed, view summaries, and stay consistent!

---

## 🔧 Features

- ✅ Add daily habits you want to track
- ✅ Mark habits as done
- 📋 View a daily summary
- 💾 (Optional) Save your progress to a JSON file
- 🌈 Terminal color output using `colorama` (optional)

---

## 📦 Getting Started

### Requirements:
- Python 3.x
- (Optional) `colorama` for colored CLI


## ✅ HABIT TRACKER CLI — TO-DO LIST

You’ll follow this **step-by-step task list** to complete the project:

---

### 🚧 **Project Setup**
- [ ] Create a new folder: `habit-tracker-cli`
- [ ] Create a Python file: `habit_tracker.py`
- [ ] (Optional) Initialize Git: `git init`
- [ ] (Optional) Create a virtual environment: `python -m venv venv`

---

### 🧱 **Phase 1 — Core Features**
> Basic habit tracker that runs in the terminal.

- [ ] Create an empty `habits = []` list
- [ ] Create an empty `status = {}` dictionary
- [ ] Create `add_habit()` function
- [ ] Create `view_habits()` function
- [ ] Create `mark_habit_done()` function
- [ ] Create `daily_summary()` function
- [ ] Build a `main_menu()` using a `while` loop and `input()`
- [ ] Handle invalid inputs cleanly with messages

---

### 🎨 **Phase 2 — UX Polish**
- [ ] Add colored outputs using `colorama` (✅, ❌)
- [ ] Add confirmation messages (e.g., “Habit added!”)

---

### 💾 **Phase 3 — Save Progress**
> Requires you to finish Python’s file handling section first.

- [ ] Learn how to use `json` module (`json.dump`, `json.load`)
- [ ] Save the `habits` list and `status` dict into a `data.json` file
- [ ] Load previous data at app startup

---

### 🧠 **Phase 4 — Nice-to-Haves**
- [ ] Add streak tracking (consecutive completions)
- [ ] Add delete/edit habit option
- [ ] Export daily report to `.txt` or print PDF
- [ ] Build a modular folder structure

---

## 📄 README.md for GitHub

Here’s a ready-made README file you can copy-paste:

---

```markdown
# 🧠 Habit Tracker CLI (Python)

A simple command-line application built in Python to help track your daily habits. Mark them as completed, view summaries, and stay consistent!

---

## 🔧 Features

- ✅ Add daily habits you want to track
- ✅ Mark habits as done
- 📋 View a daily summary
- 💾 (Optional) Save your progress to a JSON file
- 🌈 Terminal color output using `colorama` (optional)

---

## 📦 Getting Started

### Requirements:
- Python 3.x
- (Optional) `colorama` for colored CLI

### Install colorama
```bash
pip install colorama
```

### Run the app
```bash
python habit_tracker.py
```

---

## 📁 Project Structure
```
habit-tracker-cli/
├── habit_tracker.py
├── data.json         # (Optional) Save progress
└── README.md
```

---

## 🌱 Future Plans

- [ ] Add streaks
- [ ] Export daily summary
- [ ] REST API version (FastAPI)

---

## 💡 Why I Built This

To learn:
- Core Python (loops, dicts, input/output)
- File I/O and logic structuring
- Real-world CLI apps

---

## 🧑‍💻 Built By
*VIKNESH S R* — aspiring Backend/AI developer 🚀

---
