# Rock Paper Scissors Game

This is a simple and fun Rock-Paper-Scissors Web App built using **Python (Flask)** and **HTML/CSS/JavaScript**.
It allows users to:

-Play Rock, Paper, Scissors
-See results with animations
-View a leaderboard stored in SQLite (`leaderboard.db`)

This project demonstrates how Flask communicates with frontend JS, how to send user choices to the backend, and how to store scores.

---

## Live Demo (Deployed on Render)

**Live Website:** https://rock-paper-scissors-using-python-html.onrender.com

### Screenshot 

<img width="1828" height="917" alt="home page" src="https://github.com/user-attachments/assets/ae497d90-3113-4c29-8a3e-cdfbcaa279cf" />

---

## Features
### Play Game
-Choose Rock / Paper / Scissors → Flask decides result.

### Sound Effects
-Sound effects for mouse click, win, lose and tie.

### Lottie Animations
-Added animations for winning, losing, and tying.

### Leaderboard
-Stores user scores in SQLite (leaderboard.db).

---

## Technologies Used
-**Python (Flask)**
-**HTML / CSS / JavaScript**
-**SQLite Database**
-**Render (for hosting)**

---

## Run Locally
### Install Dependencies
pip install -r requirements.txt

### Run Flask App
python rock_paper_scissor.py

### Open in Browser
Go to: http://127.0.0.1:5000/

---

## Notes
-Leaderboard data is stored in `leaderboard.db`.

### Screenshot of leaderboard
<img width="1841" height="942" alt="leaderboard" src="https://github.com/user-attachments/assets/eeeaeb2a-6d3b-40b0-aa98-87d1e758e0e9" />

### -If the database is empty, run:

  python db_setup.py

-All animations and sounds are inside the static/ folder.
-The frontend communicates with Flask using fetch() API in JavaScript.

---

## Purpose
###This project was created for learning:
-Flask routing
-Sending data between HTML → JS → Python
-Handling game logic on backend
-Working with SQLite



