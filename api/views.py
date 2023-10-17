import django.http
from django.contrib.auth.models import User
from ninja import NinjaAPI
from django.db import IntegrityError


from orgs.models import OSC
from users.models import Perfil
from .models import (
    OSCSchema,
    LoginSchema,
    RegisterSchema,
    JWTSchema,
    AuthBearer,
    UserSchema,
)
from .utils import generate_jwt

router = NinjaAPI()


@router.get("orgs/", response=list[OSCSchema])
def get_orgs(request):
    all_orgs = OSC.objects.all()
    return list(all_orgs)


@router.get("orgs/{id}", response=OSCSchema)
def get_org(request, id: int):
    try:
        org = OSC.objects.get(oscId=id)
    except OSC.DoesNotExist:
        raise django.http.Http404

    return org


@router.post("login/", response=JWTSchema)
def login(request, payload: LoginSchema):
    user = User.objects.get(username=payload.username)
    if user is not None and user.check_password(payload.password):
        return generate_jwt(user)

    return django.http.HttpResponse(status=401)


@router.post("register/", response=JWTSchema)
def register(request, payload: RegisterSchema):
    print(payload)

    try:
        user = User.objects.create_user(
            payload.username,
            password=payload.password,
            email=payload.email,
            first_name=payload.first_name,
            last_name=payload.last_name,
        )
    except IntegrityError:
        return django.http.HttpResponse(status=400)
    else:
        perfil = Perfil(usuario=user, telefono=payload.phone)
        perfil.save()

    return generate_jwt(user)


@router.get("users/me/", response=UserSchema, auth=AuthBearer())
def get_user(request):
    return request.auth
