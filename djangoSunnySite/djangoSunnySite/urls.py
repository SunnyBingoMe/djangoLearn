"""djangoSunnySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^webapp/', include('webapp.urls')),
    #url(r'^blog/', include('blog.urls')),
    url(r'^api1/', include('api1.urls', namespace='rest_framework')),
    url(r'^blog2/', include('blog2.urls', namespace='blog2')),
    url(r'^upload/', include('upload.urls', namespace='upload')),
    url(r'^', include('blog2.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # influencing http-get & display media files (in browser) seems unmatched urls will try match here, not influencing uploading
