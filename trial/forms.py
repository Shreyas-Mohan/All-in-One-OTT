from django import forms
from .models import content

class contentForm(forms.Form):
   content = forms.ModelChoiceField(queryset=content.objects.all(), label='select content of your choice')
