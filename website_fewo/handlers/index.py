from flask import render_template, redirect, url_for, request
from flask_mail import Mail, Message
from threading import Thread
from ..app import app


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['email'] is not None and request.form['name'] is not None and request.form['message'] \
                is not None:
            msg = Message("Anfrage zur Ferienwohnung von: " + request.form['name'],
                          sender=request.form['email'],
                          recipients=['fewo.rhein@gmail.com'])
            sent_by = "Die Anfrage wurde gesendet von: " + request.form['name'] + " und dessen Kontakt-Mail Adresse: " \
                      + request.form['email'] + "\n\n"
            message = "Seine/Ihre Nachricht ist die Folgende: \n\n" + request.form['message']
            msg.body = sent_by + message

            if len(request.form['emailSPAM']) == 0:
                Thread(target=send_async_email, args=(app, msg)).start()
                return render_template("message_send.html")

            return render_template("errors/404.html")
        else:
            return render_template('message_us_error.html')
    else:
        return render_template('index.html')


@app.route('/')
def goto_frontpage():
    return redirect(url_for('index'))


@app.route('/impressum')
def impressum():
    return render_template('impressum.html')


@app.route('/dsgvo')
def dsgvo():
    return render_template('dsgvo.html')


def send_async_email(app, msg):
    mail = Mail(app)
    with app.app_context():
        mail.send(msg)
