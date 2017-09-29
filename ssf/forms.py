from django import forms
from .models import *


class SenateSeedFundForm(forms.Form):
    activity = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    ssf = forms.IntegerField(label='Fund Amount')
    council = forms.ChoiceField(choices=COUNCIL, widget=forms.Select)
    entity = forms.CharField()
