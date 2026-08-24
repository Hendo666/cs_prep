from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("movies.db")
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        watched INTEGER DEFAULT 0)
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()

    html = """
    <html>
    <head>
        <style>
            body {
            font-family: Arial, sans-serif;
            background-color: #1a1a2e;
            margin: 40px;
            color: #eee;
            }
            gradient {
            background-image: linear-gradient(to right, black, white)}
            h1 {
            color: #e94560;
            }
            input[type="text"] {
            background-color: #16213e;
            color: white;
            padding: 10px;
            width: 200px;
            border: 1px solid #e94560;
            border-radius: 5px;
            margin-right: 5px;
            }
            button {
            padding: 10px 15px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px 20px;
            cursor: pointer;
            }
            button:hover {
            background-color: #2980b9;
            }
            a {
            color: white;
            background-color: #2ecc71;
            text-decoration: none;
            padding: 5px 10px;
            border-radius: 20px;
            margin-left: 5px;
            }
            a:hover {
            opacity: 0.8;
            }
            a.delete{
            background-color: #e74c3c;
            }
            ul {
            list-style-type: none;
            padding: 0;
            }
            li {
            background-color: #16213e;
            color: white;
            margin: 5px;
            padding: 10px;
            border-radius: 8px;
            width: 400px;
            display: flex;
            justify-content: space-between;}
        </style>
    </head>
    </html>
    """
    html += '<h1>My Movie Watchlist</h1>'
    html += '<form method="POST" action="/add">'
    html += '<input type="text" name="title" placeholder="Movie Title" required>'
    html += '<input type="text" name="genre" placeholder="Genre" required>'
    html += '<button type="submit">Add Movie</button>'
    html += '</form>'

    html += "<ul>"
    for movie in movies:
        if movie[3] == 1:
            status = "Watched"
        else:
            status = "Not watched"
        html += f"<li>{movie[1]} ({movie[2]}) - {status} "
        html += f"<a href='/watch/{movie[0]}'>Mark Watched</a>"
        html += f"<a class='delete' href='/delete/{movie[0]}'>Delete</a></li>"
    html += "</ul>"

    return html

@app.route("/add", methods=["POST"])
def add_movie():
    title = request.form["title"]
    genre = request.form["genre"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (title, genre) VALUES (?, ?)", (title, genre))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

@app.route("/watch/<int:id>")
def watch_movie(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET watched = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

@app.route("/delete/<int:id>")
def delete_movie(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    create_table()
    app.run(debug=True)