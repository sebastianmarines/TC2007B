import django.http
from django.contrib.auth.models import User
from ninja import NinjaAPI
from jose import jwt

SECRET = 'secret'

from orgs.models import OSC
from .models import OSCSchema, LoginSchema

router = NinjaAPI()


@router.get('orgs/', response=list[OSCSchema])
def get_orgs(request):
    all_orgs = OSC.objects.all()
    return list(all_orgs)


@router.get('orgs/{id}', response=OSCSchema)
def get_org(request, id: int):
    try:
        org = OSC.objects.get(oscId=id)
    except OSC.DoesNotExist:
        raise django.http.Http404

    return org


@router.post('login/')
def login(request, payload: LoginSchema):
    user = User.objects.get(username=payload.username)
    if user is not None and user.check_password(payload.password):
        token = jwt.encode({'username': user.username}, SECRET, algorithm='HS256')
        return {'token': token}

    return django.http.HttpResponse(status=401)
