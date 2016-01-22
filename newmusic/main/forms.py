from django.forms import ModelForm
from django import forms

from newmusic.main.models import Opinion

class OpinionForm(ModelForm):
    opinion = forms.BooleanField(required=False)

    class Meta:
        model = Opinion
        fields = ['opinion', 'artist']

    # def form_valid(self, form):
    #     form.user = self.request.user
    #     form.artist = self.request.artist
    #     return super(OpinionForm, self).form_valid(form)
