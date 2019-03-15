from ..app import app
import os
from flask import render_template, redirect, url_for, request
from website_fewo.model.email import send_email


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['email'] is not None and request.form['name'] is not None and request.form['message'] \
                is not None:
            message = "" + request.form['email'] + "says: " + request.form['message']
            send_email("Email von: " + request.form['name'], sender=request.form['email'],
                       recipients=[os.environ.get('MAIL_USERNAME')], text_body=message)
            return render_template('message_send.html')
        else:
            return render_template('message_us_error.html')
    else:
        return render_template('index.html')


@app.route('/')
def goto_frontpage():
    return redirect(url_for('index'))
