from curses.ascii import US
from tkinter import CASCADE
from MySQLdb import Timestamp
from django.utils.timezone import now
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=10000)
    author=models.CharField(max_length=30)
    slug=models.CharField(max_length=130,default='')
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return self.title

# Model for comment
class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Blog,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    Timestamp=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.comment[0:10]+"... by "+self.user.username