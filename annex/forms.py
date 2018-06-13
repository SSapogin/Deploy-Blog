from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'placeholder': 'Имя'}))
    sender = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'E-mail получателя', 'type' : 'email'}))
    comments = forms.CharField(widget = forms.widgets.Textarea(attrs={'cols': 40, 'rows': 5, 'placeholder' : 'Комментарий'}))
