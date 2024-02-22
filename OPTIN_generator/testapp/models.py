from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=1000)
    create_at=models.DateField(auto_now_add=True)
    img=models.ImageField(null=True, upload_to='media')
