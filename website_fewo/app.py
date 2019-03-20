from flask import Flask
from website_fewo.config import Config
import os
import logging
import configparser
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

CURRENT_DIR = os.path.abspath(os.getcwd())
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(MODULE_DIR, 'static')
TEMPLATES_PATH = os.path.join(MODULE_DIR, 'templates')
app.config.from_object(Config)

try:
    config = configparser.ConfigParser()
    config.read(STATIC_PATH + '/mail.conf')
    mail_username = config['DEFAULT']['gmail_user_name']
    mail_password = config['DEFAULT']['gmail_password']

    app.config.update(dict(
        # EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME=mail_username,
        MAIL_PASSWORD=mail_password
    ))
except KeyError:
    app.logger.error("Mail config file could not be found! Sending emails via form has been disabled!")
    app.config.update(
        # EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME="username_not_available",
        MAIL_PASSWORD="password_not_available"
    )

if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/fewo_logs', maxBytes=5012, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Fewo-Website')

from . import handlers