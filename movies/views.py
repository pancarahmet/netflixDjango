from django.shortcuts import render
from .models import *
from user.models import Profiles
from django.db.models import Q

# Create your views here.

def anaSayfa(request):
    return render(request,"index.html")
def hesap(request):
    return render(request,"hesap.html")
def browse_index(request):
    filmler=Movies.objects.all()
    serach_movie=""
    if request.GET.get("search_movie"):
        serach_movie=request.GET.get("search_movie")
        filmler=filmler.filter(
            Q(filmismi__icontains=serach_movie) |
            Q(katagori__name__icontains=serach_movie) |
            Q(tur__name__icontains=serach_movie)
            )
    context={}
    # print("izleyen "+Izlenenler.objects.get(user=request.user))
    try:
        izleyen=Izlenenler.objects.get(user=request.user)
        izlenen=izleyen.izlenen.all()
        context={
            "izlenen":izlenen,
            "filmler":filmler,
            "search_movie":serach_movie
        }
        
    except:
        context={
            "filmler":filmler,
            "search_movie":serach_movie
        }
    return render(request,"browse-index.html",context)

def profiles(request):
    kullanicilar=Profiles.objects.filter(owner= request.user)
    context={
        "kullanici":kullanicilar
    }
    return render(request, "browse.html",context)
