from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        date_joined = self.request.query_params.get('date_joined')
        if date_joined:
            queryset = queryset.filter(date_joined=date_joined)
        return queryset