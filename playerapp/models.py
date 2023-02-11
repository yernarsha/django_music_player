from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    audio_file = models.FileField()

    def __str__(self):
        return self.title
