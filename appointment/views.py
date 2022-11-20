from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import render
from .models import DoctorsAppointment
from .serializers import DoctorsAppointmentSerializer
from api.utils import send_admin_notifications

# @custom_view_decorator


@api_view(['POST'])
def DoctorAppointment(request):
    if request.method == 'POST':
        serializer = DoctorsAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = "Please confirm Doctors Appointment"
            send_admin_notifications(msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
