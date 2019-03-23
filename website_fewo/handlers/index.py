from flask import render_template, redirect, url_for, request
from website_fewo.model import email
from ..app import app


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['email'] is not None and request.form['name'] is not None and request.form['message'] \
                is not None:
            sent_by = "Die Anfrage wurde gesendet von: " + request.form['name'] + " und dessen Kontakt-Mail Adresse: " \
                      + request.form['email'] + "\n\n"
            message = "Seine/Ihre Nachricht ist die Folgende: \n\n" + request.form['message']

            email.send_email("Fewo Rhein:Nachricht von: " + request.form['name'], sender=request.form['email'],
                             recipients=['fewo.rhein@gmail.com'], text_body=sent_by + message)
            return render_template('message_send.html')
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
