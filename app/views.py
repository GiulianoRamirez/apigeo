from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import json
import urllib.request

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from app.models import coordenadasAgresor


@csrf_exempt
def ingresarCoordenadasAgresor(request):
    lat = request.GET["lat"]
    lng = request.GET["lng"]

    agresor = coordenadasAgresor.objects.get(id="1")
    agresor.lat = lat
    agresor.lng = lng
    
    agresor.save()

    return HttpResponse("Coordenadas del agresor modificadas correctamente lat: "+lat+"lng: "+lng)

    

@csrf_exempt
def getCoordenadasAgresor(request):

    agresor = coordenadasAgresor.objects.get(id="1")

    data = {
        "lat": agresor.lat,
        "lng": agresor.lng, 
    }
    
    datajson = json.dumps(data)

    return HttpResponse(datajson)

    
