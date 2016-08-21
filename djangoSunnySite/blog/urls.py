from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post # we need a DB table/model named "Post"

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by("-date")[:25],
                                template_name = "blog/blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
                                             template_name = 'blog/post.html')),
    # '?P' is a named (capturing) group. 'pk' means primary-key.   https://docs.djangoproject.com/en/1.9/topics/http/urls/#named-groups
]
