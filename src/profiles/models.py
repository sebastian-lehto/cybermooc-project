from django.db import models

class User(models.Model):
	username = models.TextField()
	uid = models.IntegerField()
