from flask import Flask
import os
import logging
from logging.handlers import RotatingFileHandler
from website_fewo import errors

app = Flask(__name__)

if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/fewo_logs', maxBytes=5012, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Fewo-Website')

from . import handlers