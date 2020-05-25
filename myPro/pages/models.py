from django.db import models

# Create your models here.
class Command(models.Model):
    command = models.CharField(max_length=130)
