from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Euan's Web Server is LIVE</h1>"

if __name__ == "__main__":
    app.run(debug=True)