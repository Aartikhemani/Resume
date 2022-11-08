from django.shortcuts import render

# Create your views here.
from main.models import *


def index(request):
    home = Home.objects.latest('update')
    about = About.objects.latest('update')
    profile = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    context = {
        'home': home,
        'about': about,
        'profile': profile,
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def contactView(request):
    home = Home.objects.latest('update')
    about = About.objects.latest('update')
    profile = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    context = {
        'home': home,
        'about': about,
        'profile': profile,
        'categories': categories,
    }
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data = Contact(name=name,email=email,message=message)
        data.save()

    return render(request, 'main/index.html', context)