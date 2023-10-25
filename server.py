from flask import Flask, send_from_directory, request
import sqlite3
import json

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

# Path to connect to our database
@app.route("/login", methods=['POST'])
def login():
    # login to a database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # load data from request
    data =  json.loads(request.get_data())
    # fetch password from database
    r = c.execute(f"SELECT Password FROM ACCOUNTS WHERE Username='{data['username']}'")
    fetched_password = r.fetchone()
    print(data['password'] == fetched_password[0])
    return {
        "valid_password": data['password'] == fetched_password[0],
    }

# Path to fetch, i.e. SELECT
@app.route("/fetch")
def fetch():
    # connect to database
    connection = sqlite3.connect('StockTreeDB.db')
    c = connection.cursor()
    # execute a function to select from the database
    r = c.execute("SELECT * FROM STOCK")
    return str(r.fetchall())

if __name__ == "__main__":
    app.run(debug=True)