from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(max_length=13)
    desc=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)