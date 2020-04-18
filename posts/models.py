from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import  Like

# Create your models here.


User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=140)
    create_at = models.DateField(auto_now=True)
    create_of = models.DateField(auto_now=True)
    likes = GenericRelation(Like)


    def __str__(self):
        return self.body

    @property
    def total_likes(self):
        return self.likes.count()



