from django.contrib.auth.models import User
from jose import jwt

SECRET = "secret"


def generate_jwt(user: User):
    token = jwt.encode({"username": user.username}, SECRET, algorithm="HS256")
    return {"token": token}


def decode_jwt(token: str):
    return jwt.decode(token, SECRET, algorithms="HS256")
