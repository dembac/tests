from django.shortcuts import render

from .models import Claire, Lieudit
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.http import HttpResponse

class lieudittlist(TemplateView):
    template_name="ld.html"

def lieudit_dataset(request):
    mali= serialize('geojson',Lieudit.objects.all())
    return HttpResponse(mali, content_type= 'json')

class lieuditMapView(TemplateView):
    template_name = "ld.html"





class clairelist(TemplateView):
    template_name="claire.html"

def claire_dataset(request):
    mali= serialize('geojson',Claire.objects.all())
    return HttpResponse(mali, content_type= 'json')

class claireMapView(TemplateView):
    template_name = "claire.html"