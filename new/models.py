from django.db import models


class index(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birt_date = models.DateField()
    email = models.EmailField(max_length = 100)
    
# Create your models here.
