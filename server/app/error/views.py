import json
from flask import Blueprint, jsonify

error = Blueprint('error', __name__)

@error.app_errorhandler(403)
def forbidden(_):
    return jsonify(code=403, error="forbidden")

@error.app_errorhandler(404)
def page_not_found(_):
    return jsonify(code=404, error="page not found")


@error.app_errorhandler(500)
def internal_server_error(_):
    return jsonify(code=500, error="internal server error")

@error.app_errorhandler(Exception)
def all_exception_handler(e):
    return jsonify(code=500, error=str(e))