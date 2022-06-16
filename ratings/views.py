from operator import imod
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from users.models import Profile
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

def index(request):
    projects = Project.objects.all()
    return render(request,'ratings/index.html',{"projects":projects})

def searchproject(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Project.objects.filter(title__icontains=title).all()
        params = {
            'results': results
            
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any profile"
    return render(request, 'search.html')

@login_required(login_url='log_user')   
def addProject(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid:
            newProj = form.save(commit = False)
            newProj.user = user_profile
            newProj.save()
        return redirect('home')  
    else:
        form = projectForm()
    return render(request,'newProject.html',{'form':form})    

def projects(request,id):
    proj = Project.objects.get(id = id)
    return render(request,'readmore.html',{"projects":proj})


@login_required(login_url='log_user')   
def rate(request,id):

    project = Project.objects.get(id = id)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.projects = project
            rate.save()
            return redirect('home')
    else:
        form = RateForm()
    return render(request,"rate.html",{"form":form,"project":project})     