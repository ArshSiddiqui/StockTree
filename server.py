from flask import Flask, send_from_directory
import sqlite3

app = Flask(__name__)
connection = 0
c = 0

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/connect")
def connect():
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    return "Successfully Connected!"


if __name__ == "__main__":
    app.run(debug=True)