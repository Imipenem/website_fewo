from flask_mail import Message, Mail
from ..app import app
from threading import Thread


def send_async_mail(app, msg):
    with app.app_context():
        mail = Mail(app)
        mail.send(msg)


def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    Thread(target=send_async_mail, args=(app, msg)).start()
