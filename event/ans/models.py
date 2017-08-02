from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User) #extending user model
	score=models.IntegerField(default=0)
	name=models.CharField(max_length=200)
	phone=models.BigIntegerField(null=True)
	email=models.EmailField()
	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username

class Question(models.Model):
	number = models.IntegerField()
	answer = models.CharField(max_length=50)
	marks = models.IntegerField(null=True)

	def __str__(self):
		return str(self.number) #+ ' : ' + self.answer