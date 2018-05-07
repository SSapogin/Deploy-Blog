from django.views.generic import ListView, DetailView
from annex.models import Company, Work
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #path('', ListView.as_view(queryset=Company.objects.all().order_by("name"),template_name="annex/company.html")),
    url(r'^$', views.company),
    url(r'(?P<pk>\d+)$', DetailView.as_view(model=Company,template_name="annex/full-company.html")),
    url(r'^logout/$', views.logout),
]
