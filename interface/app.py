import sqlite3
from flask import Flask, render_template

def conn():
    dbconn = sqlite3.connect('database.db')
    dbconn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
