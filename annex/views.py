from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from annex.models import Work, Company, Specification, Materials, Factory
from django.contrib.auth.models import User
from django.contrib import auth
from annex.forms import *

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def company(request):
    all_post = Company.objects.all().order_by("name")
    all_spetific = Specification.objects.all().order_by("date_push")
    all_materials = Materials.objects.all()
    all_factory = Factory.objects.all()
    context = {"post_objects" : all_post, "specific_objects" : all_spetific, "materials_objects" : all_materials, "factory_objects" : all_factory}
    return render(request, "annex/company.html", context)

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
