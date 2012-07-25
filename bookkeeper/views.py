# Create your views here.
from django.shortcuts import render_to_response

from bookkeeper.models import *
from django.http import HttpResponse

def index(request):
    farmerList = Farmer.objects.all()
    return render_to_response('bookkeeper/index.html', {'farmerList': farmerList})

