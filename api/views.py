from django.shortcuts import render
from .models import Doctors, Services, Faqs, Appointments, CallDoctors, CallAppointments
from .serializers import DoctorSerializer, ServiceSerializer, FaqsSerializer, AppointmentSerializer, CallAppointmentSerializer, CallDoctorSerializer
from rest_framework import viewsets, pagination
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def service_list(request):
    if request.method == 'GET':
        services = Services.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def services_detail(request, pk):
    try:
        services = Services.objects.get(pk=pk)
    except Services.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(services)
        return Response(serializer.data)


@api_view(['GET'])
def faqs_list(request):
    if request.method == 'GET':
        faqs = Faqs.objects.all()
        serializer = FaqsSerializer(faqs, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# def doctors_list(request):
#     if request.method == 'GET':
#         doctors = Doctors.objects.all()
#         serializer = DoctorSerializer(doctors, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def doctors_detail(request, pk):
#     try:
#         doctors = Doctors.objects.get(pk=pk)
#     except Doctors.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DoctorSerializer(doctors)
#         return Response(serializer.data)


# @api_view(['GET'])
# def call_doctors_list(request):
#     if request.method == 'GET':
#         call_doctors = CallDoctors.objects.all()
#         serializer = CallDoctorSerializer(call_doctors, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def call_doctors_detail(request, pk):
#     try:
#         call_doctors = CallDoctors.objects.get(pk=pk)
#     except CallDoctors.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CallDoctorSerializer(call_doctors)
#         return Response(serializer.data)


class PageSizePagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "size"


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctors.objects.all().order_by('-id')
    serializer_class = DoctorSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all().order_by('-id')
    serializer_class = AppointmentSerializer


class CallDoctorViewSet(viewsets.ModelViewSet):
    queryset = CallDoctors.objects.all().order_by('-id')
    serializer_class = CallDoctorSerializer


class CallAppointmentViewSet(viewsets.ModelViewSet):
    queryset = CallAppointments.objects.all().order_by('-id')
    serializer_class = CallAppointmentSerializer
