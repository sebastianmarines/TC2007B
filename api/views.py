import django.http
from ninja import NinjaAPI
from orgs.models import OSC
from .models import OSCSchema
from ninja import NinjaAPI

from orgs.models import OSC
from .models import OSCSchema

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
