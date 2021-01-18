from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Recipie(models.Model):
	title = models.CharField(max_length=100)
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
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
  
class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
	instagram_url = models.CharField(max_length=100, blank=True, null=True)
	facebook_url = models.CharField(max_length=100, blank=True, null=True)
	twitter_url = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('theblog:home')


class Comment(models.Model):
	recipie = models.ForeignKey(Recipie, related_name="comments", on_delete= models.CASCADE)
	name = models.CharField(max_length=100)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	ordering = ['-id']

	def __str__(self):
		return '%s - %s' % (self.recipie.title, self.name)
