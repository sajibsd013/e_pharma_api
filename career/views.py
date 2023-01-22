from django.shortcuts import render
from .models import Job
from .serializers import JobSerializer
from rest_framework import viewsets, pagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import randrange
# Create your views here.


@api_view(['GET','POST'])
def job_list(request):
    if request.method == 'GET':
        job = Job.objects.all()
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)




@api_view(['GET'])
def job_detail(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)

