from django.forms import ModelForm

from newmusic.main.models import Opinion

class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        fields = ['opinion']

    def form_valid(self, form):
        form.user = self.request.user
        return super(OpinionForm, self).form_valid(form)
