from flask import Flask, request, render_template
import sqlite3

DB_PATH = '/opt/note_app/notes.db'
app = Flask(__name__)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    init_db()
    if request.method == "POST":
        note = request.form["note"]
        conn = sqlite3.connect(DB_PATH)
        conn.execute("INSERT INTO notes (content) VALUES (?)", (note,))
        conn.commit()
        conn.close()

    conn = sqlite3.connect(DB_PATH)
    notes = conn.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
