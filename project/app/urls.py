from django.urls import path
from . import views
urlpatterns = [
    path('students', views.studetns),
    path('students/<int:id>/', views.studentDetails),

    path('users', views.Users.as_view()),
    path('users/<int:id>/',views.UserDetails.as_view()),

    path('employers/', views.Employees.as_view()),
    path('employers/<int:pk>/', views.EmployeeDetails.as_view())
]
