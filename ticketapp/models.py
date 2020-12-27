from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Department(models.Model):
   dept_name = models.CharField(max_length=64)
class Employee(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    username = models.CharField(max_length=64, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    dedpartment = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept')
    #section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="sect")



