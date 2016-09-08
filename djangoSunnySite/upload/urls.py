# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^upload_media/$', upload_media, name='upload_media'),
    url(r'^multi_file_field/$', FileFieldView.as_view(), name='multi_file_field'),
]
