from ..app import app
import os
from flask import render_template, redirect, url_for, request
from flask_mail import Mail, Message
from website_fewo import mail
from website_fewo.model.forms import validate_email


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if validate_email(request.form['email']) and request.form['name'] is not None and request.form['message'] \
                is not None:
            msg = Message("Email von: " + request.form['name'], sender=request.form['email'],
                          recipients=[os.environ.get('MAIL_USERNAME')])
            sent_by = "Mail von " + request.form['email']
            message = "Seine message: " + request.form['message']
            msg.body = sent_by + message
            mail.send(msg)
            return render_template('message_send.html')
        else:
            return render_template('message_us_error.html')
    else:
        return render_template('index.html')


@app.route('/')
def goto_frontpage():
    return redirect(url_for('index'))
