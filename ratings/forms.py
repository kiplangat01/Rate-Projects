from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Rating, Project



class projectForm(forms.ModelForm):

  class Meta:
    model = Project
    fields = ['title', 'image', 'description', 'technologies']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']