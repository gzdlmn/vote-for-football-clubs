from django.shortcuts import render,redirect
from . models import Club,Club1player,Club2player
from . forms import ClubForm,Club1playerForm,Club2playerForm
import subprocess
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home_page(request):
    current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    current_machine_ids_list = []
    no1 = Club.objects.filter(club_name= '1').count()
    no2 = Club.objects.filter(club_name='2').count()
    no3 = Club.objects.filter(club_name='3').count()
    no4 = Club.objects.filter(club_name='4').count()
    no5 = Club.objects.filter(club_name='5').count()
    no6 = Club.objects.filter(club_name='6').count()
    no7 = Club.objects.filter(club_name='7').count()
    no8 = Club.objects.filter(club_name='8').count()
    no9 = Club.objects.filter(club_name='9').count()
    no10 = Club.objects.filter(club_name='10').count()
    form = ClubForm(request.POST or None)
    if form.is_valid():
        club = form.save(commit=True)
        if club.club_name == '1':
            return redirect("club:real-madrid")
        elif club.club_name == '2':
            return redirect("club:barcelona")
        return redirect("home")
    return render(request, "home.html", {"form": form, "no1": no1, "no2": no2, "no3": no3, "no4": no4, "no5": no5, "no6": no6,
                                         "no7": no7, "no8": no8, "no9": no9, "no10": no10, "current_machine_id":current_machine_id})

def real_madrid(request):
    form = Club1playerForm(request.POST or None)
    if form.is_valid():
        club1player = form.save(commit=False)
        club1player.save()
        return redirect("home")
    return render(request, "real-madrid.html", {"form":form})

def barcelona(request):
    form = Club2playerForm(request.POST or None)
    if form.is_valid():
        club2player = form.save(commit=False)
        club2player.save()
        return redirect("home")
    return render(request, "barcelona.html", {"form":form})