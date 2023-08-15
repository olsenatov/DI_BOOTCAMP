from django.shortcuts import render
from .serializers import PostSerializer
# from django.views.decorators.csrf import csrf_exempt #decorator for testing purposes
from .models import Report
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsForecaster

class ReportView(APIView):
    
    permission_classes = (IsForecaster,)
    def get(self, request, *args, **kwargs ):
        reports = Report.objects.all()
        serializer = PostSerializer(reports, many=True)
        return Response(data=serializer.data)
    
    def delete(self, request, pk, *args, **kwargs):
        report = report.objects.get(id = pk)
        
        self.objects_check_permissions(request, report)
        
        report.delete()
        
        return Response({'message' : f'Report id {pk} DELETED'})
        