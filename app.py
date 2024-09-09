import os
from flask import Flask, render_template, redirect
import threading, time, requests
app = Flask(__name__)
keep_alive_thread = None
view_count = 0

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
