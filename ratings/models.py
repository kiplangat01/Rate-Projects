from pydoc import describe
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    projectimage = CloudinaryField('images')
    projecturl= models.URLField(max_length=200)
    datecreated= models.DateField(auto_now_add=True )

    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    


    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()

RATE_CHOICES = [
(1,'1- Trash'),
(2,'2- Horrible'),
(3,'3- Terrible'),
(4,'4- Bad'),
(5,'5- Ok'),
(6,'6- Watchable'),
(7,'7- Good'),
(8,'8- Very Good'),
(9,'9- perfect'),
(10,'10- Master Piece'),
]

class Rating(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    projects = models.ForeignKey(Project,on_delete = models.CASCADE, related_name='reviews')
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=5000,blank=True)
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default= 0)
    usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    


    def __str__(self):
        return self.user.username