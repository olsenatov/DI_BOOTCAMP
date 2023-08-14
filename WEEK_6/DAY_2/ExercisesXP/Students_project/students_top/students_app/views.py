from django.shortcuts import render
from django.shortcuts import render
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt #decorator for testing purposes
from .models import Student
from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Student_ListView(APIView):
    def get(self, request, *args, **kwargs ):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs ):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  #show the errors of the serializer

class Student_detailView(APIView):
     def get(self, request, pk, *args, **kwargs):
        try:
            students = Student.objects.get(id=pk)
            serializer = StudentSerializer(students)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
     def put(self, request, pk, *args, **kwargs):
         student = Student.objects.get(id = pk)
         serializer = StudentSerializer(instance=student, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors)
        
     def delete(self, request, pk, *args, **kwargs):
         student = Student.objects.get(id = pk)
         student.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
