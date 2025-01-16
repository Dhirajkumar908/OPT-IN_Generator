from django.db import models
from django.contrib.auth.models import User


class HeaderFooter(models.Model):
    name=models.CharField(max_length=100)
    header=models.ImageField(upload_to='media')
    footer=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


# Create your models here.
class OptIN(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField()
    data=models.CharField(max_length=10)
    HeaderFooter=models.ForeignKey(HeaderFooter,on_delete=models.DO_NOTHING, null=True)
    # header=models.ImageField(upload_to='media')
    # footer=models.ImageField(upload_to='media')
    
class User_account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    credit=models.IntegerField()

