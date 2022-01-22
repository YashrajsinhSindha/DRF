from django.urls import path
from .api import EmployeeApi, EmployeeCreateApi, EmployeeDeleteApi, EmployeeUpdateApi

urlpatterns=[
    path('api',EmployeeApi.as_view()),
    path('api/create',EmployeeCreateApi.as_view()),
    path('api/delete/<int:pk>',EmployeeDeleteApi.as_view()),
    path('api/update/<int:pk>',EmployeeUpdateApi.as_view()),
]