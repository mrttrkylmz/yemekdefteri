from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Recipies(models.Model):
    recipie_header= models.CharField(max_length=100)
    recipie_details= models.CharField(max_length=3000)
    recipie_upvotes= models.IntegerField(default=0)
    recipie_downvotes= models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.recipie_header



class Comments(models.Model):
    recipie = models.ForeignKey(Recipies, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=300)
    comment_upvotes= models.IntegerField(default=0)
    comment_downvotes= models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.comment_text
    
    
