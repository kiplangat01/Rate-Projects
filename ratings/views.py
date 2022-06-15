from operator import imod
from django.shortcuts import render
from .models import Project
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

def index(request):
    '''
    View for the homepage
    '''
    title = "home"
    projects = Project.objects.all().order_by('-pk')
    context = {
        "title":title,
        "projects":projects,
    }
    
    return render(request,"ratings/index.html",context)

@login_required
def Upload_Project(request):
    '''
    function to upload project for display
    '''
    current_user = request.user
    if request.method == "POST":
        form = ProjectUploadForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            return redirect('index')
    else:
        form = ProjectUploadForm()
    context = {
        "form":form
    }

    return render(request,"ratings/upload.html",context)

@login_required
def Rateproject(request,pk):
    '''
    Display a single projrct and  provide ratings for it.
    '''
    project = Project.objects.get(id=pk)
    title = 'Rating'
    project_rating = Ratings.objects.filter(project=project).order_by('pk')
    current_user = request.user
    current_user_id = request.user.id
    project_rated = Ratings.objects.filter(user=current_user_id)
    
    
    
    design_mean_rating = []
    for d_rating in project_rating:
        design_mean_rating.append(d_rating.design)
    try:
        design_average = sum(design_mean_rating)/len(design_mean_rating)
        design_percent = design_average * 10
    except ZeroDivisionError:
        design_average = "0"
        design_percent = 0
      
        
    content_mean_rating = []
    for c_rating in project_rating:
        content_mean_rating.append(c_rating.content)
    try:
        content_average = sum(content_mean_rating)/len(content_mean_rating)
        content_percent = content_average * 10
    except ZeroDivisionError:
        content_average = "0"
        content_percent = 0
        
    
    
    usability_mean_rating = []
    for u_rating in project_rating:
        usability_mean_rating.append(u_rating.usability)
    try:
        usability_average = sum(usability_mean_rating)/len(usability_mean_rating)
        usability_percent = usability_average *10
    except ZeroDivisionError:
        usability_average = "0"
        usability_percent = 0
        
        
    form = RatingUploadForm()

    context = {
        "project":project,
        "form":form,
        "project_rating":project_rating,
        "design_average":design_average,
        "content_average":content_average,
        "usability_average":usability_average,
        "usability_percent":usability_percent,
        "content_percent":content_percent,
        "design_percent":design_percent
    }

    return render(request,"ratings/projectrating.html",context)