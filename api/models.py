from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from ninja import ModelSchema, Schema
from ninja.security import HttpBearer

from orgs.models import Tag, OSC
from .utils import decode_jwt


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        print(f"Authenticating with token: {token}")
        payload = decode_jwt(token)
        try:
            user = User.objects.get(username=payload["username"])
        except ObjectDoesNotExist:
            return None
        else:
            return user


class TagSchema(ModelSchema):
    class Config:
        model = Tag
        model_fields = "__all__"


class OSCSchema(ModelSchema):
    tags: list[TagSchema]

    class Config:
        model = OSC
        model_exclude = [
            "tags",
            "videos",
            "imagenes",
            "articulosInteres",
            "redesSociales",
        ]
        depth = 1

class OSCEditSchema(ModelSchema):
    class Config:
        model = OSC
        model_fields = ["coordenadas_latitud", "coordenadas_longitud"]


class JWTSchema(Schema):
    token: str


class LoginSchema(Schema):
    username: str
    password: str


class RegisterSchema(LoginSchema):
    email: str
    phone: str
    first_name: str
    last_name: str


class UserSchema(ModelSchema):
    phone: str

    class Config:
        model = User
        model_fields = ["username", "first_name", "last_name", "email"]
        depth = 1

    @staticmethod
    def resolve_phone(user: User):
        return user.perfil.telefono


class ErrorSchema(Schema):
    message: str


class MapInfoSchema(Schema):
    oscs: list[OSCSchema]
    tags: list[TagSchema]
