from django import forms
from .models import Log

class LogForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Log
        fields = ['title', 'content', 'image']
