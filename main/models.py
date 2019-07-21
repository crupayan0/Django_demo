from django.db import models
from datetime import datetime

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    song_uploaded_on = models.DateTimeField('Uploaded on', default = datetime.now())

