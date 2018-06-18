from django.views.generic import ListView, DetailView
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #path('', ListView.as_view(queryset=Company.objects.all().order_by("name"),template_name="annex/company.html")),
    url(r'^$', views.courses),
    url(r'^about/', views.about),
    url(r'^blog-home/', views.blogH),
    url(r'^blog-single/', views.blogS),
    url(r'^contact/', views.contact),
    url(r'^event-details/', views.event),
    url(r'^events/', views.events),
    url(r'^gallery/', views.gallery),
    url(r'^register/', views.register),
    url(r'^signin/', views.signin),
    #url(r'(?P<pk>\d+)$', DetailView.as_view(model=Company,template_name="annex/full-company.html")),
    url(r'^logout/$', views.logout),
]
