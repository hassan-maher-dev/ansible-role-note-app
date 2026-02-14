# app.py
from flask import Flask, render_template_string, request
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
DB_FILE = 'notes.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note_content = request.form.get('content')
        if note_content:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("INSERT INTO notes (content, timestamp) VALUES (?, ?)", (note_content, timestamp))
            conn.commit()
            conn.close()
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT content, timestamp FROM notes ORDER BY id DESC")
    notes = c.fetchall()
    conn.close()
    
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Note Taking App</title>
        <style>
            body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .note { border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
            .time { color: #666; font-size: 0.8em; }
            textarea { width: 100%; height: 100px; }
            button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>📝 Simple Note Taking App</h1>
        <form method="post">
            <textarea name="content" placeholder="Write your note here..."></textarea><br><br>
            <button type="submit">Save Note</button>
        </form>
        <hr>
        {% for note in notes %}
            <div class="note">
                <div class="time">🕒 {{ note[1] }}</div>
                <div class="content">📌 {{ note[0] }}</div>
            </div>
        {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(html, notes=notes)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80)