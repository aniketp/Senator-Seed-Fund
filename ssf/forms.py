from django import forms
from .models import *


class SenateSeedFundForm(forms.Form):
    activity = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    ssf = forms.IntegerField(label='Fund Amount')
    council = forms.ChoiceField(choices=COUNCIL, widget=forms.Select)
    entity = forms.CharField()


class AddSenatorForm(forms.Form):
    username = forms.CharField(help_text='Please exclude "@iitk.ac.in"')
    session = forms.ChoiceField(choices=SESSION, widget=forms.Select)
    max_fund = forms.IntegerField(label='Grant', max_value=10000)


class ContributeFundForm(forms.Form):
    amount = forms.IntegerField(max_value=10000)