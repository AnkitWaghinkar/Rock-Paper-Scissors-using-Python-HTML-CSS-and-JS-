from flask import Flask, request, render_template, session, redirect
import random, sqlite3, time

app = Flask(__name__)
app.secret_key = "secret_123"

# -------------------------------------------- #
#  Leaderboard Database Function
# -------------------------------------------- #
def update_leaderboard(name, result):
    conn = sqlite3.connect("leaderboard.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM leaders WHERE name=?", (name,))
    row = cur.fetchone()

    if not row:
        cur.execute("""
            INSERT INTO leaders (name, wins, losses, ties, total)
            VALUES (?, 0, 0, 0, 0)
        """, (name,))
        conn.commit()

    if result == "win":
        cur.execute("UPDATE leaders SET wins = wins + 1, total = total + 1 WHERE name=?", (name,))
    elif result == "lose":
        cur.execute("UPDATE leaders SET losses = losses + 1, total = total + 1 WHERE name=?", (name,))
    else:
        cur.execute("UPDATE leaders SET ties = ties + 1, total = total + 1 WHERE name=?", (name,))

    conn.commit()
    conn.close()


# -------------------------------------------- #
# Determine Game Result
# -------------------------------------------- #
def determine_game_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie", "tie"

    win_map = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if win_map[player_choice] == computer_choice:
        return "You Win", "win"

    return "You Lose", "lose"


# -------------------------------------------- #
#  Home Route — Game Page
# -------------------------------------------- #
@app.route("/", methods=["GET", "POST"])
def home():
    session.setdefault("player_score", 0)
    session.setdefault("computer_score", 0)
    session.setdefault("sound", True)

    computer_choice = ""
    animation = ""
    result = ""

    if request.method == "POST":
        time.sleep(1.2)

        player_name = request.form.get("player_name", "Guest")
        player_choice = request.form["choice"].lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        result, animation = determine_game_result(player_choice, computer_choice)

        update_leaderboard(player_name, animation)

        if result == "You Win":
            session["player_score"] += 1
        elif result == "You Lose":
            session["computer_score"] += 1

    return render_template(
        "index.html",
        result=result,
        animation=animation,
        computer=computer_choice,
        sound=session["sound"],
        player_score=session["player_score"],
        computer_score=session["computer_score"]
    )


# -------------------------------------------- #
#  Toggle Sound
# -------------------------------------------- #
@app.route("/toggle_sound")
def toggle_sound():
    session["sound"] = not session["sound"]
    return redirect("/")


# -------------------------------------------- #
#  Leaderboard Page
# -------------------------------------------- #
@app.route("/leaderboard")
def leaderboard():
    conn = sqlite3.connect("leaderboard.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT name, wins, losses, ties, total
        FROM leaders
        ORDER BY wins DESC
        LIMIT 10
    """)
    rows = cur.fetchall()
    conn.close()
    return render_template("leaderboard.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
