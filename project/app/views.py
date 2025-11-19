from django.shortcuts import render
from .models import Student, Employee
from .serializer import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import mixins , generics
# Create your views here.


#api_view  in function based

@api_view(['GET', 'POST'])
def studetns(request):
    if request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.error)
            return Response(serializer.error)
        
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetails(request, id):
    student=get_object_or_404(Student, id=id)

    if request.method == 'GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
    elif request.method=='DELETE':
        student.delete()
        return Response()



# class based view

from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializer import UserSerializer

class Users(APIView):
    def get(self, request):
        users=User.objects.all()
        serializer=UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    
class UserDetails(APIView):
    
    def get_user (self,id):
        return get_object_or_404(User, id=id)
    
    def get(self,request, id):
        user=self.get_user(id=id)
        serializer=UserSerializer(user)
        return Response(serializer.data)
    
    def put(self,request, id):
        user=get_object_or_404(User, id=id)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(slef, request, id):
        user=get_object_or_404(User, id=id)
        user.delete()
        return Response()
    

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class EmployeeDetails(mixins.UpdateModelMixin, mixins.RetrieveModelMixin,  mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self, request,pk):
        return self.retrieve(request,pk)
    
    def put(self, request, pk):
        return self.update(request,pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)