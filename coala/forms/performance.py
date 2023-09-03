from django import forms
from ..models import Performance

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['performance', 'registered_datetime']
