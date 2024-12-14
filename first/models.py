from django.db import models

# Create your models here.
class RandomHistory(models.Model):
    text = models.CharField(max_length=10)
    created_date = models.DateTimeField()
