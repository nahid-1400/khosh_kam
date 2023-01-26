"""khosh_kam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from malile_khosh_kam.views import MalileDetail, AllMalile, MalileSearch, MalileCateGory, advanced_filter, malile_favorites

app_name = 'malile_khosh_kam'

urlpatterns = [
    path('malile/<malile_id>/', MalileDetail.as_view(), name='malile_detail'),
    path('maliles', AllMalile.as_view(), name='all-maliles'),
    path('maliles/page/<int:page>', AllMalile.as_view(), name='all-maliles'),
    path('search', MalileSearch.as_view(), name='malile-search'),
    path('search/page/<int:page>', MalileSearch.as_view(), name='malile-search'),
    path('category/<slug>', MalileCateGory.as_view(), name='malile-category'),
    path('category/<slug>/page/<int:page>', MalileCateGory.as_view(), name='malile-category'),
    path('advanced_filter', advanced_filter, name='advanced-filter'),
    path('malile_favorites/<malile_id>', malile_favorites, name='malile-favorites'),
]
