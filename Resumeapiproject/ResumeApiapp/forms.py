from django import forms
from ResumeApiapp.models import Resumeapi

#creating resume api form
class ResumeapiForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    graduation = forms.CharField(max_length=30)
    skills = forms.CharField(max_length=100)
    experience =forms.FloatField()
    aboutus = forms.CharField(max_length=200)
    resume = forms.CharField(max_length=500)

class Meta():
    model = Resumeapi
    fields = '__all_'
