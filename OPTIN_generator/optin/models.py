from django.db import models




class HeaderFooter(models.Model):
    Name=models.CharField(max_length=20)
    header=models.ImageField(upload_to='media')
    footer=models.ImageField(upload_to='media')

    def __str__(self):
        return self.Name


# Create your models here.
class OptIN(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField()
    data=models.DateField()
    HeaderFooter=models.ForeignKey(HeaderFooter,on_delete=models.DO_NOTHING, null=True)
    # header=models.ImageField(upload_to='media')
    # footer=models.ImageField(upload_to='media')
    
