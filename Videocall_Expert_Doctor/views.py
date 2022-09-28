from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from e_pharma_api.view_decorator import custom_view_decorator

from django.shortcuts import render
from .models import VideoCallExpertDoctor, VideoCallExpertDoctorsAppointment
from .serializers import VideoCallExpertDoctorSerializer, VideoCallExpertsAppointmentSerializer

# Create your views here.


# @custom_view_decorator
@api_view(['GET'])
def doctors_list(request):
    if request.method == 'GET':
        doctors = VideoCallExpertDoctor.objects.all()
        serializer = VideoCallExpertDoctorSerializer(doctors, many=True)
        return Response(serializer.data)


# @custom_view_decorator
@api_view(['GET'])
def doctors_detail(request, pk):
    try:
        doctors = VideoCallExpertDoctor.objects.get(pk=pk)
    except VideoCallExpertDoctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoCallExpertDoctorSerializer(doctors)
        return Response(serializer.data)


# @custom_view_decorator
@api_view(['POST'])
def appointment(request):
    if request.method == 'POST':
        serializer = VideoCallExpertsAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
