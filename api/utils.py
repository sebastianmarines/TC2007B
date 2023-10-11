from django.http import HttpResponse
from jose import jwt
from django.contrib.auth.models import User

SECRET = "secret"


def generate_jwt(user: User):
    token = jwt.encode({"username": user.username}, SECRET, algorithm="HS256")
    return {"token": token}
