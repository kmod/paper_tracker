from django.db import models

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=255)
