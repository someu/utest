from flask import (Blueprint, jsonify)
from flask_jwt_extended import (
    create_access_token
)

from app import db
from app.email import send_email
from app.models import User
from app.decorators import validate, auth

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
@validate({
    "email": {"type": "string"},
    "password": {"type": "string"}
})
def login(data):
    user = User.query.filter_by(email=data['email']).first()
    if user is not None and user.password_hash is not None and \
            user.verify_password(data['password']):
        token = create_access_token(user.id)
        return jsonify(code=200, token=token)
    else:
        return jsonify(code=200, error='邮箱/密码错误')


@account.route('/info', methods=['GET', 'POST'])
@auth()
def info(user=None):
    data = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "role_id": user.role_id
    }
    return jsonify(code=200, data=data)
