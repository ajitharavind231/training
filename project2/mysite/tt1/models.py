import datetime
from pyexpat import model
from sre_constants import MAX_REPEAT
from unicodedata import name
from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=20,null=print("Error"),primary_key=True)
    phone_no=models.IntegerField();

class manager(models.Model):
    work_place=models.ForeignKey(place, on_delete=models.CASCADE)
    mgr_name=models.CharField(max_length=20)
    mgr_dob=models.CharField(max_length=8)




