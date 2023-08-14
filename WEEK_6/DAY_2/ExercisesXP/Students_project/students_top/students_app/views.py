from django.shortcuts import render
from django.shortcuts import render
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt 
from .models import Student
from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
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
     
#daily_challenge 
@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        date_joined_param = request.GET.get('date_joined')
     
        if date_joined_param:
            try:
                date_joined = datetime.strptime(date_joined_param, '%Y-%m-%d').date()
                students = Student.objects.filter(date_joined=date_joined)
            except ValueError:
                return JsonResponse({'error': 'Invalid date format'}, status=400)
        
            return JsonResponse({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=400)
        else:
            students = Student.objects.all()
            
        student_data = [{'first name' : student.first_name, 'last name' : student.last_name, 'email' : student.email, 'date_joined' : student.date_joined} for student in students]
        return JsonResponse({'students' : student_data})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405) 

#can't understand if it really filters by date, as the dates of joining are basically the same

