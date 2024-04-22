from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite database file
DATABASE = 'users.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Insert some dummy users for the challenge
def insert_dummy_users():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('admin', 'AdminPassword123'))
    conn.commit()
    conn.close()

# Insert dummy users
insert_dummy_users()

# Check credentials
def authenticate(username, password):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    blacklist = ["or", "and", "true", "false", "union", "like", "=", ">", "<", ";", "--", "/*", "*/"]

    # Check if any of the blacklist keywords are present in username or password
    for keyword in blacklist:
        if keyword in username or keyword in password:
            conn.close()
            return None

    # Check if the provided username and password match the database
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()

    conn.close()
    return user

# Login page route
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate(username, password)
        if user:
            return redirect(url_for('success'))
        else:
            error = 'Invalid credentials'
    return render_template('login.html', error=error)

# Success page route
@app.route('/success')
def success():
    return "Congratulations! You've successfully logged in.\n Flag: DD24{bypassing_WAF_1s_n0t_4lw4ys_3asy}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=False)
