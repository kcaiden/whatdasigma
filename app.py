import os
from flask import Flask, render_template, redirect
import threading, time, requests
app = Flask(__name__)
keep_alive_thread = None
view_count = 0

def keep_alive():
    while True:
        requests.get("https://caiden.onrender.com/admin")
        print("Keep alive")
        time.sleep(300)

keep_alive_thread = threading.Thread(target=keep_alive)
keep_alive_thread.start()

@app.route('/.well-known/discord')
def discord_verification():
    return "dh=a27f5b61f9ec7f646d0173055006c9d98263083a"

@app.route('/')
def home():
    global view_count
    view_count += 1
    return render_template('index.html')


@app.route('/view_count')
def get_view_count():
    return f"View count: {view_count}"


@app.route('/admin')
def root():
   return render_template('index.html')
