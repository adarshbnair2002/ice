from django.db import models
from good.models import *

# Create your models here.
class cartlist(models.Model):
   cart_id=models.CharField(max_length=122,unique=True)
   date_addded=models.DateTimeField(max_length=122)

   def __str__(self):
    return self.cart_id

class items(models.Model):
   prodt=models.ForeignKey(products,on_delete=models.CASCADE)
   cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
   quan=models.IntegerField()

   def __str__(self):
    return self.prodt



  