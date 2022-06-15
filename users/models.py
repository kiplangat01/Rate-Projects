from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    picture = CloudinaryField('image', default='default.jpg', null=True)
    # picture = models.ImageField( upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


        