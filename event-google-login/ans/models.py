from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	score=models.IntegerField(default=0)
	def __str__(self):
		return self.username

class Question(models.Model):
	number = models.IntegerField()
	answer = models.CharField(max_length=50)
	marks = models.IntegerField(null=True)

	def __str__(self):
		return str(self.number) #+ ' : ' + self.answer