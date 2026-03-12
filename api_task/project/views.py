from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
# Create your views here.


@api_view(['POST'])
def create_project(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.error, status=400)


@api_view(['GET'])
def list_project(request):
    status = request.GET.get('status')
    if status:
        projects = Project.objects.filter(status=status)
    else:
        project = Project.objects.all()


    serializer = ProjectSerializer(project,many=True)

    return Response(serializer.data)



@api_view(['GET'])
def project_details(request, id):
    project = Project.objects.get(id=id)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)



@api_view(['PUT'])
def update_project(request, id):
    project = Project.objects.get(id=id)
    serializer = ProjectSerializer(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return Response({"message": "Deleted"})