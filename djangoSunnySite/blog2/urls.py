from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^edit/create/$', views.PostCreate.as_view(), name='post-create'),
    url(r'^edit/update/(?P<pk>\d+)/$', views.PostUpdate.as_view(), name='post-update'),
    url(r'^edit/delete/(?P<pk>\d+)/$', views.PostDelete.as_view(), name='post-delete'),
]
