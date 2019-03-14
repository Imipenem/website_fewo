from ..app import app
from flask import render_template, redirect, url_for


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/')
def goto_frontpage():
    return redirect(url_for('index'))
