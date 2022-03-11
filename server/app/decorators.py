from functools import wraps
from flask import abort, request
from flask_login import current_user
from app.models import Permission
import jsonschema
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity
)
from app.models.user import User


def validate(schema):
    """校验请求参数，校验成功后将data作为参数传给view函数"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            data = request.get_json()
            args = request.args.to_dict()
            instance = {}
            instance.update(data)
            instance.update(args)
            target_schema = {
                "type": "object",
                "required": list(schema.keys()),
                "properties": schema
            }
            try:
                jsonschema.validate(instance=instance, schema=target_schema)
                return f(*args, **kwargs, data=instance)
            except Exception as e:
                raise e

        return decorated_function

    return decorator


def auth(permission=0):
    """jwt 认证，认证成功后将user作为参数传给view函数"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            verify_jwt_in_request()
            current_uid = get_jwt_identity()
            try:
                user = User.query.filter_by(id=current_uid).first()
                if user == None:
                    raise Exception('用户不存在')
                if permission and not user.can(permission):
                    raise Exception('权限不足')

                return f(*args, **kwargs, user=user)
            except Exception as e:
                raise e

        return decorated_function

    return decorator
