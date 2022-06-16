from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Rating, Project



class projectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','projectimage','projecturl']
    
class RateForm(forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ['text','design','usability','content']