from django.db import models
from django.contrib.auth.models import User

class categories(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(max_length=200,null=False,blank=False)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class bestsellers(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    actual_price= models.IntegerField(null=False)
    selling_price=models.IntegerField(null=False)
    description=models.TextField(max_length=300,null=False)
    image=models.ImageField(upload_to='images',null=True)
    quantity=models.BigIntegerField(null=False,blank=False)

    def __self__(self):
        return self.name
    
class products(models.Model):
    category=models.ForeignKey(categories,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False,blank=False)
    actual_price= models.IntegerField(null=False)
    selling_price=models.IntegerField(null=False)
    description=models.TextField(max_length=300,null=False)
    image=models.ImageField(upload_to='images',null=True)
    quantity=models.BigIntegerField(null=False,blank=False)

