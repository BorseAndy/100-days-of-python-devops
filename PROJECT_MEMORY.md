# 🧠 Project Memory

**Last Updated:** 2026-03-12
**Course Status:** Day 25 Completed / Next: Day 26 (List/Dict Comprehension)

**Accumulated Key Concepts:**
- **Python Fundamentals (Days 1-10):** Data types, control flow, functions.
- **Scope & Debugging (Days 11-15):** Variable management and troubleshooting.
- **OOP (Days 16-17, 20-23):** Class modeling, inheritance (`Turtle`), logical encapsulation.
- **File I/O (Day 24):** Reading/Writing to local files (`open()`, `read()`, `write()`).
- **Data Analysis with Pandas (Day 25):**
    - Reading/Writing CSVs (`read_csv`, `to_csv`).
    - DataFrames vs Series.
    - Filtering data rows: `data[data.state == "Ohio"]`.
    - Extracting scalar values with `.item()`.
    - Converting columns to lists with `.to_list()` for efficient lookups.
    - List comprehensions for data filtering (e.g., finding missing states).

**Current Focus (Day 25):**
- [x] Setting up Day 25 directory structure.
- [x] Understanding CSV handling (File I/O vs `csv` module vs `pandas`).
- [x] Data manipulation with Pandas (filtering rows, accessing columns).
- [x] Creating DataFrames from scratch and exporting to CSV.
- [x] Central Park Squirrel Census Data Analysis.
- [x] U.S. States Game (using Pandas and Turtle).

**Open Notes/Bugs:**
- *Pandas Tip:* Always use `.item()` when you need a single primitive value (int/string) from a filtered row to avoid index-related errors.
- *Best Practice:* Refactor main loops to load data once and use English for all code symbols to ensure long-term maintainability.

**Next Steps (Day 26+):**
- **Day 26:** List and Dictionary Comprehension (Advanced Pythonic patterns).
- **Day 27:** GUI Development with Tkinter and `*args`/`**kwargs`.
