from django.shortcuts import render
from django.views.generic import ListView, DetailView
from malile_khosh_kam.models import Malile, CateGory

def home(request):
    new_malile = Malile.objects.active_malile().order_by('-id')
    return render(request, 'khosh_kam/home.html', context={'new_malile': new_malile})

def header_base(request):
    category = CateGory.objects.category_active()
    return render(request, 'khosh_kam/base/header_base.html', context={'category': category})