from flask import Blueprint

blueprint = Blueprint('errors', __name__)

from website_fewo.errors import error_handlers
