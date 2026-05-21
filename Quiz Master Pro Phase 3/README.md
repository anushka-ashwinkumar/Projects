# Quiz Master Pro (CMS Edition) 🎮📝

An advanced, persistent Command-Line Interface (CLI) trivia system built in Python. This version features a fully integrated Content Management System (CMS) that allows users to create, view, delete, and store questions dynamically using an external text file database.

## 🚀 Features

* **Persistent Storage File System:** Leverages Python File I/O (`open()`, `write()`, `readlines()`) to save quiz data inside a localized database (`questions.txt`), preserving text data permanently across executions.
* **Full CRUD Management:** Offers a robust administrative text menu allowing users to seamlessly append new content, stream existing items to screen layout, or securely drop elements via specific list positions.
* **Corrupt Data Filtering:** Automatically sanitizes database ingestion by skipping empty entries or incorrectly formatted pipes (`|`), preventing terminal crashes mid-game.
* **Fault-Tolerant File Verification:** Implements a proactive structural `try/except` handler catching potential `FileNotFoundError` scenarios gracefully.
* **Dynamic Gameplay Modifiers:** Allows users to input customized strings, choose to `skip` challenging queries without penalty, and view structural breakdown metrics using dynamic percentage configurations.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Database Engine:** Plain-Text File (`.txt`) with custom structural delimiter separation (`|`)
* **Interface:** Command Line Interface (CLI)

## 📁 Required Database Format

The application maps questions and answers inside `questions.txt` using a distinct pipe separator (`|`). The file layout matches this structure:

```text
What is the capital of France?|Paris
Which planet is known as the Red Planet?|Mars
