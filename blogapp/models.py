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
