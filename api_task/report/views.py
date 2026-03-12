from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import daily_report
from .serializers import DailyReportSerializers


@api_view(['POST'])
def create_report(request):
    serializer = DailyReportSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors)


@api_view(['GET'])
def list_reports(request, project_id):
    date = request.GET.get('date')
    if date:
        reports = daily_report.objects.filter(project_id=project_id, date=date)
    else: 
        reports = daily_report.objects.filter(project_id=project_id)


    serializer = DailyReportSerializers(reports, many=True)
    return Response(serializer.data)

# Create your views here.
