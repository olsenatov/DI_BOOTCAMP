from rest_framework import serializers
from .models import Teacher, SchoolFacility, Laboratory

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFacility
        fields = '__all__'
        
class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'