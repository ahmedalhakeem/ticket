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
      return f"{self.section_name}"
class User(AbstractUser):
   deptartment = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dept_name", default=None, null=True)
   section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="sect_name", default=None, null=True) 
   pc_code = models.CharField(max_length=10, null=True, blank=True)

class ProblemType(models.Model):
   software = 'SW'
   hardware = 'HW'
   
   select_type = [
      (software, 'software'),
      (hardware, 'hardware'),
   ]
   problem_type = models.CharField(max_length=2, choices=select_type, default=software,)
   description = models.CharField(max_length=100, null=True, default=None)
   def __str__(self):
      return f'{self.problem_type}: {self.description} '

class Problems(models.Model):
   p_type = models.ForeignKey(ProblemType, on_delete=models.CASCADE, related_name='type')
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="has_problem", default=None)
   user_solver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="has_solution", default=None)

   status = models.BooleanField(default=False)
   date = models.DateTimeField(default=None, blank=True)

   def __str__(self):
      return f"{self.problem_type} by {self.user} on {self.user.deptartment} section {self.user.section}"