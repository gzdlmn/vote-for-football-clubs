from django import forms
from . models import Club,Club1player,Club2player

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

class Club2playerForm(forms.ModelForm):
    club2players = forms.ChoiceField(choices=Club2player.CHOICE2SPLAYER, widget=forms.RadioSelect())
    class Meta:
        model = Club2player
        fields = ['club2players']