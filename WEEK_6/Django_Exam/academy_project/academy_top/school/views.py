from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Teacher, SchoolFacility, Laboratory
from .serializers import TeacherSerializer, LabSerializer, FacilitySerializer

def course_details(request, course_id):
    course = Course.objects.all(pk=course_id)
    return Response(course)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
class SchoolFacilityListView(APIView):
    def get (self, request):
        facility = SchoolFacility.objects.all()
        serializer = FacilitySerializer(facility, many=True)
        return Response(serializer.data)

class LaboratoryListView(APIView):
    def get (self, request):
        lab = Laboratory.objects.all()
        serializer = LabSerializer(lab, many=True)
        return Response(serializer.data)