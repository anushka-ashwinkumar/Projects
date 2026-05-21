# Harry Potter Quiz Master Plus ⚡🏆

An advanced terminal-based Harry Potter trivia game built in Python. This version utilizes indexed parallel lists to manage data, handles custom program-exit states, and features a robust user-readiness workflow before launching into high-difficulty lore questions.

## 🚀 Features

* **Parallel Array/List Processing:** Uses corresponding `questions` and `answers` lists mapped together via loop indexing (`range(len(questions))`) to efficiently manage quiz content.
* **Pre-Game Readiness Workflow:** Implements an interactive onboarding checkpoint asking if the player is ready, allowing them to take their time or exit the application cleanly before the game loop starts.
* **Case-Insensitive Exact Matching:** Evaluates user responses using `.lower()` matching to keep the validation fair against strict case configurations.
* **Tiered Dynamic Score Breakdown:** Features custom performance thresholds evaluating the user's score out of 5 to display proportional achievements (`Excellent!`, `Good job`, `Not bad, keep practicing`, or `Better luck next time`).

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Interface:** Command Line Interface (CLI)

## 📦 How to Run the Project

### Prerequisites
Make sure you have Python 3 installed on your machine. 

### Setup & Execution
1. Open your terminal or command prompt.
2. Navigate into this project's folder:
   ```bash
   cd independent-project-3
