from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Department(models.Model):
   department_name = models.CharField(max_length=64, null=True, blank=True)

   def __str__(self):
      return f"{self.department_name}"

class Section(models.Model):
   section_name = models.CharField(max_length=64, null=True, blank=True)
   dept = models.ForeignKey(Department, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.section_name}, {self.dept}"
class User(AbstractUser):
   deptartment = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dept_name",)
   section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="sect_name",) 

class Problems(models.Model):
   software = 'SW'
   hardware = 'HW'
   
   select_type = [
      (software, 'software'),
      (hardware, 'hardware'),
   ]
   problem_type = models.CharField(max_length=2, choices=select_type, default=software,)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="has_problem", default=None)

   def __str__(self):
      return f"{self.problem_type} by {self.user}"