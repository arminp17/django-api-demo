from django.db import models

# Create your models here.

class Appmodel(models.Model):
    userId = models.IntegerField(default=0)
    title = models.TextField(null=True)
    body = models.TextField(null=True)