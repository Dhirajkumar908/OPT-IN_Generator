from django.db import models

# Create your models here.
class TechBlog(models.Model):
    title=models.CharField(max_length=100)
    create_at=models.DateField(auto_now_add=True)
    short_discription=models.CharField(max_length=200)
    content=models.TextField()
    img=models.ImageField(upload_to='media')