from rest_framework import serializers
from .models import Student, Employee
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
      model=Student
      fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model=User
       fields=['username', 'password']
    


class EmployeeSerializer(serializers.ModelSerializer):
   class Meta:
      model=Employee
      fields='__all__'