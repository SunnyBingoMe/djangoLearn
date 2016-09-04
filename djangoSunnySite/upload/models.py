from django.db import models


# Create your models here.
class Media(models.Model):
    filename = models.FileField(upload_to='%Y%m%d') # sub-folder in /media/
