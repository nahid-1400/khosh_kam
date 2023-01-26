from django.shortcuts import render
from django.views.generic import ListView
from about_us_khosh_kam.models import AboutUsModel

class AboutUs(ListView):
    template_name = 'about_us_khosh_kam/about_us.html'
    model = AboutUsModel

    def get_queryset(self):
        return AboutUsModel.objects.filter(active=True)
