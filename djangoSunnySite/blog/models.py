from django.db import models

class Post(models.Model): # this will create a table "Post".
    title = models.CharField(max_length = 140) # optional max_length
    body  = models.TextField()
    date  = models.DateTimeField()
    
    def __str__(self):
        return self.title

