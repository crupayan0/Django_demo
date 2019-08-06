from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

# Create your views here.
def homepage(request):
    return render(request,
                  'main/home.html',
                  {'songs': Song.objects.all})

