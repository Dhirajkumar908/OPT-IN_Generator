from django.db import models

# Create your models here.
class OptIN(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField()
    data=models.DateField()
    header=models.ImageField(upload_to='media')
    footer=models.ImageField(upload_to='media')
