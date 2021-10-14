from django import forms
from . models import Club,Club1player

class ClubForm(forms.ModelForm):
    club_name = forms.ChoiceField(choices=Club.CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Club
        fields = ['club_name']

class Club1playerForm(forms.ModelForm):
    club1players = forms.ChoiceField(choices=Club1player.CHOICE1SPLAYER, widget=forms.RadioSelect())
    class Meta:
        model = Club1player
        fields = ['club1players']