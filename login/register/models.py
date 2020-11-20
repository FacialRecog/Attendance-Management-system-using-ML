from django.db import models

from django.core.validators import RegexValidator


# Create your models here.
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    age=models.IntegerField()
    model_pic = models.ImageField(upload_to = '', default = 'none/no-img.jpg')
    
	
