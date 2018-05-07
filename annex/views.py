from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from annex.models import Work, Company
from django.contrib import auth

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def company(request):
    all_post = Company.objects.all().order_by("name")
    context = {"post_objects" : all_post}
    return render(request, "annex/company.html", context)
