from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import datetime
from xml.etree import ElementTree as ET
from pages.models import posts
from django.core.mail import send_mail, BadHeaderError
from pages.forms import *

def dollar_evro(request):
    id_dollar = "R01235"
    id_evro = "R01239"
    valuta = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req"))
    for  line in valuta.findall('Valute'):
        id_v = line.get('ID')
        if id_v == id_dollar:
            rub_dollar = line.find('Value').text
        if id_v == id_evro:
            rub_evro = line.find('Value').text
    today = datetime.date.today()
    return HttpResponse("<span class='main-header__currencies-val'>USD:</span><span id='dollar_vue'>" + rub_dollar +
    "</span><br><span class='main-header__currencies-val'>EUR:</span><span id='evro_vue'>" + rub_evro + "</span>" +
    "<script>var evro = evro_vue.innerHTML; evro = Number(evro.replace(',','.')).toFixed(2); evro_vue.innerHTML = evro;</script>" +
    "<script>var dollars = dollar_vue.innerHTML; dollars = Number(dollars.replace(',','.')).toFixed(2); dollar_vue.innerHTML = dollars;</script>")

def post_go(request):
    all_post = posts.objects.all().order_by("-date")[:18]
    context = {"post_objects" : all_post}
    return render(request, "pages/post.html", context)

def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			phone = form.cleaned_data['phone']
			message = form.cleaned_data['message']

			from_send = form.cleaned_data['from_send']
			to_send = form.cleaned_data['to_send']
			date_start = form.cleaned_data['date_start']
			date_finish = form.cleaned_data['date_finish']
			night = form.cleaned_data['night']
			adults = form.cleaned_data['adults']
			child = form.cleaned_data['child']

			recipients = ['kamelot.sapogin@gmail.com']
			try:
				send_mail('Заявка - ' + subject, 'Телефон:' + phone + '\nE-mail: ' + sender + '\nКомментарий: ' + message +
                '\n\nБлок горящих туров:\nОткуда: ' + from_send + '\nКуда: ' + to_send + '\nДаты вылета: ' + date_start + ' по ' + date_finish +
                '\nНочей: ' + night + '\nВзрослых: ' + adults + '\nДетей: ' + child, 'kamelot.sapogin@gmail.com', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'pages/thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'pages/contact.html', {'form': form})

def contactView1(request):
	if request.method == 'POST':
		form = ContactForm_num1(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			phone = form.cleaned_data['phone']
			recipients = ['kamelot.sapogin@gmail.com']
			try:
				send_mail('Обратный звонок - ' + subject, phone, 'kamelot.sapogin@gmail.com', recipients)
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return render(request, 'pages/thanks.html')
	else:
		form = ContactForm_num1()
	return render(request, 'pages/contact1.html', {'form': form})

def contactView2(request):
	if request.method == 'POST':
		form = ContactForm_num2(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			phone = form.cleaned_data['phone']
			recipients = ['kamelot.sapogin@gmail.com']
			try:
				send_mail('Запрос на информацию по туру - ' + subject, 'E-mail: ' + sender + '\nТелефон:' + phone, 'kamelot.sapogin@gmail.com', recipients)
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return render(request, 'pages/thanks.html')
	else:
		form = ContactForm_num2()
	return render(request, 'pages/contact2.html', {'form': form})

def contactView3(request):
	if request.method == 'POST':
		form = ContactForm_num3(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			phone = form.cleaned_data['phone']
			recipients = ['kamelot.sapogin@gmail.com']
			try:
				send_mail('Оформление визы - ' + subject, 'E-mail: ' + sender + '\nТелефон:' + phone, 'kamelot.sapogin@gmail.com', recipients)
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return render(request, 'pages/thanks.html')
	else:
		form = ContactForm_num3()
	return render(request, 'pages/contact3.html', {'form': form})

def contactView4(request):
	if request.method == 'POST':
		form = ContactForm_num4(request.POST)
		if form.is_valid():
			star = form.cleaned_data['star']
			country = form.cleaned_data['country']
			date_date = form.cleaned_data['date_date']
			night = form.cleaned_data['night']
			phone = form.cleaned_data['phone']
			recipients = ['kamelot.sapogin@gmail.com']
			try:
				send_mail('Подобрать тур.', 'Страна: ' + country + '\nДаты вылета: ' + date_date +
                '\nНочей:' + night + '\nТелефон: ' + phone + '\nКласс отеля от: ' + star, 'kamelot.sapogin@gmail.com', recipients)
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return render(request, 'pages/thanks.html')
	else:
		form = ContactForm_num4()
	return render(request, 'pages/contact4.html', {'form': form})
