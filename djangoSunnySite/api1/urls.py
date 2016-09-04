from django.conf.urls import url, include
from .views import PostList, PostDetail

urlpatterns = [
    # '?P' is a named (capturing) group. 'pk' means primary-key.   https://docs.djangoproject.com/en/1.9/topics/http/urls/#named-groups
    url(r'^post-s/$', PostList.as_view()),
    url(r'^post/(?P<pk>\d+)$', PostDetail.as_view()),
]
