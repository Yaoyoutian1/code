from django.db import models

# Create your models here.
class user(models.Model):
    UserId =models.IntegerField()
    UserName =models.CharField(max_length=20)
    UserImgs=models.CharField(max_length=128)
    Age=models.IntegerField()
    Sex=models.IntegerField(default=0)
    UserAutoGraph=models.CharField(max_length=50)
    CreateTime=models.DateTimeField('date published')

