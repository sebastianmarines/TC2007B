from ninja import ModelSchema, Schema

from orgs.models import Tag, OSC


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


class ErrorSchema(Schema):
    message: str