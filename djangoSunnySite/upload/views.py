from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from upload.forms import MediaForm
from .models import *


def upload_media(request):
    if request.method == 'POST':
        media_form = MediaForm(request.POST, request.FILES)
        if media_form.is_valid():
            new_file = Media(filename=request.FILES['filename'])
            new_file.save()
            return HttpResponseRedirect(reverse('upload:upload_media'))
    else:
        media_form = MediaForm()
        
    media_list = Media.objects.all()
    
    return render(
        request,
        'upload/upload_media.html',
        {'media_list': media_list,
         'media_form': media_form}
    )
