from operator import imod
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from users.models import Profile
from .forms import projectForm,RateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
import random


def index(request):
    user = request.user
    if request.method == "POST":
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            image = request.FILES.get('image')
            description = form.cleaned_data.get('description')
            technologies = form.cleaned_data.get('technologies')
            url = form.cleaned_data.get('url')

            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return HttpResponseRedirect('/')
    else:
        form = projectForm()

    try:
        posts = Project.objects.all().order_by('-date_posted')
        a_post = random.randint(0, len(posts)-1)
        random_post = posts[a_post]
        print(random_post.image)
    except Project.DoesNotExist:
        posts = None
    return render(request, 'index.html', {'posts': posts, 'form': form, 'random_post': random_post})

    
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
    return render(request, 'results.html')


@login_required(login_url='login')
def project(request, post):
    post = Project.objects.get(title=post)
    ratings = Rating.objects.filter(user=request.user, post=post).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Rating.objects.filter(post=post)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RateForm()
    params = {
        'post': post,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request,"ratings/projectrating.html",{"form":form,"project":project})     