from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("games.db")
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, title TEXT)")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    create_table()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()
    conn.close()
    
    # Build the HTML with a form
    html = """
    <html>
    <head>
        <title>My Games Library</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 40px;
            }
            h1 {
                color: #2c3e50;
            }
            input[type="text"] {
                padding: 10px;
                width: 250px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                padding: 10px 15px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #2980b9;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                background-color: white;
                margin: 5px 0;
                padding: 10px;
                border-radius: 5px;
                width: 300px;
                display: flex;
                justify-content: space-between;
            }
            a {
                color: white;
                text-decoration: none;
                padding: 5px 10px;
                border-radius: 3px;
                background-color: #e74c3c;
                margin-left: 5px;
            }
            a:hover {
                opacity: 0.8;
            }
            .edit {
                background-color: #2ecc71; /* Green */
            }
            .delete {
                background-color: #e74c3c; /* Red */
            }
        </style>
    </head>
    <body>
    """
    html += "<h1>🎮 My Games Library</h1>"
    html += '<form method="POST" action="/add">'
    html += '<input type="text" name="title" placeholder="Enter game title">'
    html += '<button type="submit">Add Game</button>'
    html += '</form>'
    html += "<ul>"
    for game in games:
        html += f"<li><span>{game[1]}</span> "
        html += f"<span><a class='edit' href='/edit/{game[0]}'>Edit</a> "
        html += f"<a class='delete' href='/delete/{game[0]}'>Delete</a></span></li> "
    html += "</ul>"
    html += "</body></html>"
    return html

@app.route("/add", methods=["POST"])
def add_game():
    title = request.form["title"]
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if the game already exists
    cursor.execute("SELECT COUNT(*) FROM games WHERE title = ?", (title,))
    count = cursor.fetchone()[0]
    
    # Only insert if it does NOT exist
    if count == 0:
        cursor.execute("INSERT INTO games (title) VALUES (?)", (title,))
        conn.commit()
    
    conn.close()
    return redirect(url_for("home"))

@app.route("/delete/<int:id>")
def delete_game(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM games WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

@app.route("/edit/<int:id>")
def edit_game(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games WHERE id = ?", (id,))
    game = cursor.fetchone()
    conn.close()

    if game: 
        html = f"""
        <h1>Edit game</h1>
        <form method="POST" action="/update/{id}">
            <input type="text" name="title" value="{game[1]}">
            <button type="submit">Save Changes</button>
        </form>
        """

        return html
    else:
        return "Game not found"

@app.route("/update/<int:id>", methods=["POST"])
def update_game(id):
    new_title = request.form["title"]
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE games SET title = ? WHERE id = ?", (new_title, id))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))
    

if __name__ == "__main__":
    app.run(debug=True)