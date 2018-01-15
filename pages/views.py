from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import datetime
from xml.etree import ElementTree as ET
from pages.models import posts
from django.core.mail import send_mail, BadHeaderError
from pages.forms import ContactForm

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
			copy = form.cleaned_data['copy']

			recipients = ['serega_s98@mail.ru']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recipients.append(sender)
			try:
				send_mail(subject, message, 'serega_s98@mail.ru', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'pages/thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'pages/contact.html', {'form': form})
