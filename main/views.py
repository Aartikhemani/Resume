from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from main.models import *


def index(request):
    home = Home.objects.latest('update')
    about = About.objects.latest('update')
    profile = Profile.objects.filter(about=about)
    social = Social.objects.all()
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()
    context = {
        'home': home,
        'about': about,
        'profile': profile,
        'social': social,
        'categories': categories,
        'portfolios': portfolios,
    }
    return render(request, 'main/index.html', context)


def contactView(request):
    home = Home.objects.latest('update')
    about = About.objects.latest('update')
    profile = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()
    context = {
        'home': home,
        'about': about,
        'profile': profile,
        'categories': categories,
        'portfolios': portfolios,
    }
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data = Contact(name=name,email=email,message=message)
        data.save()
        messages.success(request, "Thank you for your message")
        return redirect('/')
    return render(request, 'main/index.html', context)


def home(request, post_id=id):
    item =get_object_or_404(Home, id=post_id)
    return render(request, 'main/index.html',{'post':item})

def about(request, post_id=id):
    item =get_object_or_404(About, id=post_id)
    return render(request, 'main/index.html',{'post':item})

def skills(request, post_id=id):
    item =get_object_or_404(Skills, id=post_id)
    return render(request, 'main/index.html',{'post':item})

def portfolio(request, post_id=id):
    item =get_object_or_404(Portfolio, id=post_id)
    return render(request, 'main/index.html',{'post':item})

def contact(request, post_id=id):
    item =get_object_or_404(Contact, id=post_id)
    return render(request, 'main/index.html',{'post':item})

def profile(request, post_id=id):
    item =get_object_or_404(Profile, id=post_id)
    return render(request, 'main/index.html',{'post':item})

def social(request, post_id=id):
    item =get_object_or_404(Social, id=post_id)
    return render(request, 'main/index.html',{'post':item})

def category(request, post_id=id):
    item =get_object_or_404(Category, id=post_id)
    return render(request, 'main/index.html',{'post':item})