from django.db import models
from django.contrib.auth.models import User

class Recipie(models.Model):
	title = models.CharField(max_length=100)
	chef = models.ForeignKey(User, on_delete= models.CASCADE)
	recipie_details = models.TextField()


	def __str__(self):
		return self.title  +  ' | ' +  str(self.chef)
  
