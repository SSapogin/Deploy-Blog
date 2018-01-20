from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_go),
    path('course/', views.dollar_evro, name='dollar_evro'),
    url(r'^contact-1/$', views.contactView),
    url(r'^contact-2/$', views.contactView1),
    url(r'^contact-3/$', views.contactView2),
    url(r'^contact-4/$', views.contactView3),
    url(r'^contact-5/$', views.contactView4)
]
