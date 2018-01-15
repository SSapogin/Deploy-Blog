from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', ListView.as_view(queryset=posts.objects.all().order_by("-date")[:18],
    #template_name="pages/wrapper.html")),
    url(r'^$', views.post_go),
    path('course/', views.dollar_evro, name='dollar_evro'),
    url(r'^contact/$', views.contactView),
     #url(r'(?P<pk>\d+)$', DetailView.as_view(model = posts, template_name = "pages/post.html"))
]
