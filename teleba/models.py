from distutils.command.upload import upload
from msilib.schema import Class
from pyexpat import model
from tkinter import CASCADE
from django.db import models


class Services(models.Model):
    service_name=models.CharField(max_length=200)
    small_description=models.CharField(max_length=500)
    big_description=models.CharField(max_length=1000)
    service_image=models.ImageField(upload_to="",null=True,blank=True)
    def __str__(self):
        return self.service_name

class Activities(models.Model):
    activ_name=models.CharField(max_length=200)
    activ_small_description=models.CharField(max_length=200)
    activ_big_description=models.CharField(max_length=1000)
    activ_place=models.CharField(max_length=100)
    activ_date=models.DateField
    activ_image=models.ImageField(upload_to="",null=True,blank=True)
    activ_image_related1=models.ImageField(upload_to="",null=True,blank=True)
    activ_image_related2=models.ImageField(upload_to="",null=True,blank=True)
    activ_image_related3=models.ImageField(upload_to="",null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-updated', '-created']
        
    def __str__(self) :
        return self.activ_name
class Clients(models.Model):
    client_name=models.CharField(max_length=100)
    client_logo=models.ImageField(upload_to="",null=True,blank=True)
    client_description=models.CharField(max_length=200)
    client_url=models.URLField(null=True)

    def __str__(self):
        return self.client_name
class Teleba(models.Model):
    teleba_name	=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="",null=True,blank=True)   
    slogant=models.CharField(max_length=100)
    mail=models.EmailField(null=True)
    telephone=models.CharField(max_length=100)
    back_image=models.ImageField(upload_to="",null=True,blank=True)

    def __str__(self) :
        return self.teleba_name

