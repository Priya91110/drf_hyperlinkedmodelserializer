from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

class StudentListView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   
    
    
