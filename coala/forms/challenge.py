from django import forms
from ..models import Challenge

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['challenge', 'registered_datetime']

      
class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['evaluation']
