from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog2.models import Post


class IndexView(generic.ListView):
    template_name = "blog2/post_s.html"
    context_object_name = 'postS'

    def get_queryset(self):
        return Post.objects.all().order_by("-date")[:25]


class DetailView(generic.DetailView):
    template_name = "blog2/one_post.html"
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body', 'date']


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body', 'date']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog2:index')
