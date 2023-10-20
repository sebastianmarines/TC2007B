import django.http
from django.contrib.auth.models import User
from django.db import IntegrityError
from ninja import NinjaAPI

from orgs.models import OSC, Tag
from users.models import Perfil
from .models import (
    OSCSchema,
    LoginSchema,
    RegisterSchema,
    JWTSchema,
    AuthBearer,
    UserSchema,
    MapInfoSchema,
    OSCEditSchema,
    TagSchema,
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


@router.post("orgs/{id}/edit", response=OSCSchema)
def edit_org(request, id: int, payload: OSCEditSchema):
    try:
        org = OSC.objects.get(oscId=id)
    except OSC.DoesNotExist:
        raise django.http.Http404

    org.coordenadas_latitud = payload.coordenadas_latitud
    org.coordenadas_longitud = payload.coordenadas_longitud
    org.save()

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


@router.get("getMapInfo/", response=MapInfoSchema)
def get_map_info(request):
    oscs = list(OSC.objects.all())
    tags = list(Tag.objects.all())
    return MapInfoSchema(oscs=oscs, tags=tags)


@router.get("users/me/favorites/", response=list[OSCSchema], auth=AuthBearer())
def get_favorites(request):
    user = request.auth
    perfil = Perfil.objects.get(usuario=user)
    return list(perfil.favoritos.all())


@router.post("users/me/favorites/{id}/", response=OSCSchema, auth=AuthBearer())
def add_favorite(request, id: int):
    user = request.auth
    perfil = Perfil.objects.get(usuario=user)
    osc = OSC.objects.get(oscId=id)
    # Togle favorite
    if osc in perfil.favoritos.all():
        perfil.favoritos.remove(osc)
    else:
        perfil.favoritos.add(osc)
    return osc


@router.get("tags/", response=list[TagSchema])
def get_tags(request):
    return list(Tag.objects.all())