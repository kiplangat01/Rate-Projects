from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Ratings

    
class ProjectUploadForm(forms.ModelForm):
    '''
    Form to allow users upload project.
    '''
    class Meta:
        model = Project
        fields = ["title","description","link","image"]


class RatingUploadForm(forms.ModelForm):
    '''
    This class will define the form for users to rate the project
    '''
    class Meta:
        model = Ratings
        fields = ["design","usability","content"]