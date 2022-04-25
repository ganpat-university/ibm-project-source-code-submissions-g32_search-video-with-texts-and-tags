from django.db import models

# Create your models here.

from .validators import validate_video

class Video(models.Model):
    name= models.CharField(max_length=500)
    description= models.TextField()
    videofile= models.FileField(upload_to='', validators= [validate_video])

    def __str__(self):
        return self.name + ": " + str(self.videofile)