from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Recipie(models.Model):
	title = models.CharField(max_length=100)
	chef = models.ForeignKey(User, on_delete= models.CASCADE)
	#recipie_details = models.TextField()
	recipie_details = RichTextField(blank=True, null=True)
	publish_date = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name= 'recipie_post')


	def total_likes(self):
	    return self.likes.count()


	def __str__(self):
		return self.title  +  ' | ' +  str(self.chef)

	def get_absolute_url(self):
	    return reverse('theblog:recipie-detail', args=[str(self.id)])
  
