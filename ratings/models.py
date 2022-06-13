from pydoc import describe
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



class Project(models.Model):
    picture = CloudinaryField('image')
    description=models.TextField(max_length=300)
    title=models.CharField(max_length=160)
    link=models.URLField(max_length=300)
    technologies=models.CharField(max_length=200,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    date=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f'{self.user.username} {self.title} Project'

    


    def __str__(self):
        return f'{self.title}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()


    @classmethod
    def search_projects(cls,title):
        return cls.objects.filter(title__icontains=title).all()





class Ratings(models.Model):
    '''
    This model will contain the ratings for diffrent categories
    '''
    rates = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    usability = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    describtion = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def _str_(self):
        return f'{self.user.username} {self.project.title} Rating'