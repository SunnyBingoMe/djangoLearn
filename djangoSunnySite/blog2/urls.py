from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post # we need a DB table/model named "Post"
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^(?P<pk>\d+)$', views.DetailView.as_view()),
]
