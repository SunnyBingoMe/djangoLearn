from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^(?P<pk>\d+)$', views.DetailView.as_view(), name='detail'),
]
