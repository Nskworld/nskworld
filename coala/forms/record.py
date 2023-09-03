from django import forms
from ..models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['time_going_bed', 'time_falling_asleep', 'time_getting_up']
