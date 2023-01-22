from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from api.utils import send_admin_notifications
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# @custom_view_decorator





@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def DoctorAppointment(request):
    if request.method == 'POST':
        serializer = DoctorsAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = "Please confirm Doctors Appointment"
            send_admin_notifications(msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if 'user' in request.GET:
            print(request.GET['user'])
            services = DoctorsAppointment.objects.filter(
                user=request.GET['user']).order_by("-id")

        else:
            services = DoctorsAppointment.objects.all()
        serializer = DoctorsAppointmentSerializer(services, many=True)

        return Response(serializer.data)


@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def DoctorsAppointmentDetail(request, pk):
    """
    Retrieve, update or delete a code  DoctorsAppointment.
    """
    try:
        Doctors_Appointment = DoctorsAppointment.objects.get(pk=pk)
    except Doctors_Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorsAppointmentSerializer(Doctors_Appointment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DoctorsAppointmentSerializer(
            Doctors_Appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Doctors_Appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
