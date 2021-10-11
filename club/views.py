from django.shortcuts import render,redirect
from . models import Club
from . forms import ClubForm
# Create your views here.

def home_page(request):
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
    return render(request, "home.html", {"form": form, "no1": no1, "no2": no2, "no3": no3, "no4": no4, "no5": no5, "no6": no6,
                                         "no7": no7, "no8": no8, "no9": no9, "no10": no10})