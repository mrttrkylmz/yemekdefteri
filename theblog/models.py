from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Recipie(models.Model):
	title = models.CharField(max_length=100)
	chef = models.ForeignKey(User, on_delete= models.CASCADE)
	recipie_details = models.TextField()


	def __str__(self):
		return self.title  +  ' | ' +  str(self.chef)

	def get_absolute_url(self):
	    return reverse('theblog:recipie-detail', args=[str(self.id)])
  
