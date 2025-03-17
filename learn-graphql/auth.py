from datetime import datetime, timedelta
import bcrypt
import os
import jwt
from data_models import get_user


def authenticate_creds(user, password):
    password = password.encode("utf-8")
    password_hash = user.password_hash.encode("utf-8")
    return bcrypt.hashpw(password, password_hash) == password_hash


def generate_jwt(user):
    now = datetime.utcnow()
    key = os.environ["JWT_SECRET"]
    payload = {
        "iss": "avilay.rocks",
        "iat": now,
        "exp": now + timedelta(minutes=30),
        "sub": user.id,
    }
    token = jwt.encode(payload, key, algorithm="HS256")
    return token


def authenticate_token(token):
    key = os.environ["JWT_SECRET"]
    user_id = jwt.decode(
        token,
        key,
        issuer="avilay.rocks",
        algorithms="HS256",
        options={"require": ["exp", "iss", "sub"]},
    )["sub"]
    return get_user(user_id)
