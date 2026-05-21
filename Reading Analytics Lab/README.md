# Reading Analytics Lab 📚📊

An interactive personal library tracker and data visualization dashboard built in Python. This application allows avid readers to log their reading history via persistent JSON storage, query metrics, and generate dynamic graphical analytics trends using Matplotlib.

> ⚠️ **Status: Active Development (WIP)** > This project is currently being refactored to optimize runtime performance, clean up menu interfaces, and integrate the `pandas` library for advanced data manipulation.

## 🚀 Existing Features

* **JSON Storage Integration:** Implements robust File I/O using Python's `json` library (`json.load()` and `json.dump()`) to ensure user libraries save cleanly to `books.json` and persist across sessions.
* **Multi-Criteria Search Engine:** Contains flexible directory filtering, allowing users to query logs by specific Author, Genre, or Exact Title configurations.
* **On-the-Fly Library Summaries:** Instantly tracks total database entries, identifies overall rating averages, computes most-read authors, and calculates active book distributions.
* **Data Visualization Suites (Matplotlib):** Dynamically outputs analytical charts, including:
  * Bar charts tracking books per genre.
  * Line graphs tracking monthly book quantities and page thresholds.
  * Specialized breakdowns detailing top authors and average genre scores.

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Data Layer:** JSON File System System (`books.json`)
* **Visualization Engine:** Matplotlib

## 🔮 Upcoming Roadmap (Planned Upgrades)
* [ ] **Pandas Integration:** Swap dictionary comprehension loops out for high-performance Pandas DataFrames to process library aggregations.
* [ ] **Code Refactoring:** Consolidate menu structures to optimize interface switching.
* [ ] **Enhanced Input Sanitation:** Add protection against malformed date formats (`YYYY-MM-DD`).

## 📦 How to Run the Project

### Prerequisites
You need Python 3 and the `matplotlib` library installed on your machine. You can install matplotlib via your terminal using pip:
```bash
pip install matplotlib
