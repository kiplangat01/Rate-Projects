from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Ratings

    
class ProjectUploadForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ["image","title", "description",  "link", "technologies"]


class RatingUploadForm(forms.ModelForm):
    
    class Meta:
        model = Ratings
        fields = ["rates", "usability", "description"]