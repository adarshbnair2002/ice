from distutils.command.upload import upload
from django.db import models

class  Contact(models.Model):
   name=models.CharField(max_length=122)
   email=models.CharField(max_length=122)
   phone=models.CharField(max_length=122)
   date=models.DateField()

   def __str__(self):
    return self.name

class  Register(models.Model):
   name=models.CharField(max_length=122)
   email=models.CharField(max_length=122)
   phone=models.CharField(max_length=122)

   def __str__(self):
    return self.name

class  categ(models.Model):
   name=models.CharField(max_length=122)

   def __str__(self):
    return self.name

class  products(models.Model):
   name=models.CharField(max_length=122)
   img=models.ImageField(upload_to ='product')
   desc=models.TextField(max_length=122)
   
   available=models.BooleanField(max_length=122)
   
   category=models.ForeignKey(categ,on_delete=models.CASCADE)

   def __str__(self):
    return self.name
   



