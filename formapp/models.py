from django.db import models

class Reg(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    cpassword=models.CharField(max_length=15)
    mailid=models.EmailField()
    mobno=models.IntegerField()