from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from upload.forms import *
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


# this will create one record for each file in db table. http://www.evernote.com/l/AJCOlMEuQLJOlJQ72gQ224av_TcB8Lzh6kk/
class FileFieldView(FormView, ListView):
    form_class = FileFieldForm
    template_name = 'upload/multi_file_field.html'
    success_url = '/upload/multi_file_field'
    context_object_name = 'media_list'

    def get_queryset(self):
        return Media.objects.all()

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('multi_file_field')
        if form.is_valid():
            for one_file in files:
                new_file = Media(
                    filename=one_file
                )
                new_file.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
