from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model): # this will create a table "blog_post" in small letter format: "<app_name>_<class_name>"
    title = models.CharField(max_length = 140) # optional max_length
    body  = models.TextField()
    date  = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('blog2:detail', kwargs={'pk': self.pk}) # form inserted into db, then redirect to this url.
    
    def __str__(self):
        return self.title
