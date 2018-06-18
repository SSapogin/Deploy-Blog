from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from annex.models import Courses, EventAdmin, News, GalleryAdmin
from django.contrib.auth.models import User
from django.contrib import auth
from annex.forms import *

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def courses(request):
    all_post = Courses.objects.all().order_by("name")
    all_event = EventAdmin.objects.all().order_by("name")
    all_news = News.objects.all().order_by("name")
    context = {"post_objects" : all_post, "news_objects" : all_news, "all_event" : all_event,}
    return render(request, "annex/wrapper.html", context)

def blogS(request):
    all_post = Courses.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/blog-single.html", context)

def blogH(request):
    all_post = Courses.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/blog-home.html", context)

def about(request):
    all_post = Courses.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/about.html", context)

def contact(request):
    all_post = Courses.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/contact.html", context)

def event(request):
    all_post = Courses.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/event-details.html", context)

def events(request):
    all_post = Courses.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/events.html", context)

def gallery(request):
    all_post = GalleryAdmin.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/gallery.html", context)

def register(request):
    all_post = Courses.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/register.html", context)

def signin(request):
    all_post = Courses.objects.all().order_by("name")
    context = {"post_objects" : all_post,}
    return render(request, "annex/includes/signin.html", context)

def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			comments = form.cleaned_data['comments']
			recipients = ['kamelot53.sapogin@yandex.ru']
			try:
				send_mail(subject, comments, sender, recipients)
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return render(request, 'annex/thanks.html')
	else:
		form = ContactForm()
	return render(request, 'annex/contact.html', {'form': form})
