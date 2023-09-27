from django.shortcuts import render
from ninja import NinjaAPI
from orgs.models import OSC, Tag, Multimedia
from .models import OSCSchema


router = NinjaAPI()


@router.get('orgs/', response=list[OSCSchema])
def get_orgs(request):
    all_orgs = OSC.objects.all()
    return list(all_orgs)
