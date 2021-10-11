from django import forms
from . models import Club

class ClubForm(forms.ModelForm):
    club_name = forms.ChoiceField(choices=Club.CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Club
        fields = ['club_name']