from django.shortcuts import render
from django.http import HttpResponse

from funko_api.models import Funko
from funko_api.serializers import FunkoSerializer
from django.http import JsonResponse


# Create your views here.
"""
def index(request):
    return HttpResponse("OK")
"""

def get_all_funkos():
    funkos = Funko.objects.all().order_by('number')
    funkos_serializers = FunkoSerializer(funkos, many=True)
    return funkos_serializers.data

def index(request):
    funkos = get_all_funkos()
    return render(request, "index.html", {"funkos": funkos})

def about(request):
    return render(request, "about.html")

def funkos_rest(request):
    funkos = get_all_funkos()
    return JsonResponse(funkos, safe=False)

def users_rest(request):
    return JsonResponse("Ok", safe=False)


