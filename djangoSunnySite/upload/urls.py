# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import upload_media

urlpatterns = [
    url(r'^upload_media/$', upload_media, name='upload_media')
]
