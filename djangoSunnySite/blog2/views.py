from django.views import generic
from blog2.models import Post


class IndexView(generic.ListView):
    template_name = "blog2/post_s.html"
    context_object_name = 'postS'

    def get_queryset(self):
        return Post.objects.all().order_by("-date")[:25]


class DetailView(generic.DetailView):
    template_name = "blog2/one_post.html"
    model = Post
