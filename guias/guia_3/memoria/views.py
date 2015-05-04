from django.http import HttpResponse
from memoria.models import Perfil, Dificultad, Puntaje
from django.core import serializers
# Create your views here.

def getDificultades(request):
    html = serializers.serialize('json',Dificultad.objects.all())
    return HttpResponse(html)

