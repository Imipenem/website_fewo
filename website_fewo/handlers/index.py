from ..app import app
from flask import render_template, redirect, url_for, request
from website_fewo.model.forms import validate_email


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if validate_email(request.form['email']) and request.form['name'] is not None and request.form['message'] \
                is not None:
            return render_template('message_send.html')
        else:
            return render_template('message_us_error.html')
    else:
        return render_template('index.html')


@app.route('/')
def goto_frontpage():
    return redirect(url_for('index'))
