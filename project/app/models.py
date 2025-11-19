from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=10)
    roll_no=models.CharField(max_length=20)
    course=models.CharField(max_length=10)


class Employee(models.Model):
    e_id=models.CharField(max_length=50)
    name=models.CharField("employee name" , max_length=50)
