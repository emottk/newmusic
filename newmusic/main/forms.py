from django.forms import ModelForm
from django import forms

from newmusic.main.models import Opinion

class OpinionForm(ModelForm):
    opinion = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Opinion
        fields = ['opinion', 'artist']
        widgets = {'artist': forms.HiddenInput()}
