from django import forms

class ContactForm(forms.Form):
	from_send = forms.CharField(required=False, widget = forms.TextInput(attrs = {'type': 'hidden', 'id' : 'from_send', 'value' : ''}))
	to_send = forms.CharField(required=False, widget = forms.TextInput(attrs = {'type': 'hidden', 'id' : 'to_send', 'value' : ''}))
	date_start = forms.CharField(required=False, widget = forms.TextInput(attrs = {'type': 'hidden', 'id' : 'date_start', 'value' : ''}))
	date_finish = forms.CharField(required=False, widget = forms.TextInput(attrs = {'type': 'hidden', 'id' : 'date_finish', 'value' : ''}))
	night = forms.CharField(required=False, widget = forms.TextInput(attrs = {'type': 'hidden', 'id' : 'night', 'value' : ''}))
	adults = forms.CharField(required=False, widget = forms.TextInput(attrs = {'type': 'hidden', 'id' : 'adults', 'value' : ''}))
	child = forms.CharField(required=False, widget = forms.TextInput(attrs = {'type': 'hidden', 'id' : 'child', 'value' : ''}))

	subject = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'placeholder': 'Имя'}))
	sender = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder': 'E-mail', 'type' : 'email'}))
	phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'telephonetext', 'placeholder': 'Телефон'}))
	message = forms.CharField(widget = forms.Textarea(attrs = {'placeholder': 'Комментарий'}))

class ContactForm_num1(forms.Form):
	subject = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'placeholder': 'Имя'}))
	phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'telephonetext', 'placeholder': 'Телефон'}))

class ContactForm_num2(forms.Form):
	subject = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'placeholder': 'Ваше имя'}))
	sender = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder': 'Ваш e-mail', 'type' : 'email'}))
	phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'telephonetext', 'placeholder': 'Ваш телефон'}))

class ContactForm_num3(forms.Form):
	subject = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'placeholder': 'Ваше имя'}))
	sender = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder': 'Ваш e-mail', 'type' : 'email'}))
	phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'telephonetext', 'placeholder': 'Ваш телефон'}))

class ContactForm_num4(forms.Form):
	star = forms.CharField(widget = forms.TextInput(attrs = {'type': 'hidden', 'id' : 'star_inp', 'value' : ''}))
	country = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Россия'}))
	date_date = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': '9 янв - 18 янв'}))
	night = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': '6 - 14'}))
	phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'telephonetext', 'placeholder': 'Ваш телефон'}))
