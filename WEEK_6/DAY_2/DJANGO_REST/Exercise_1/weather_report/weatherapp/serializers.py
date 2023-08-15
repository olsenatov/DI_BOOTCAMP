from rest_framework import serializers
from .models import Report

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report
        fields = ('forecaster', 'location', 'temperature', 'created_at', 'type')
        
        