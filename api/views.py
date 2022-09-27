from django.shortcuts import render
from .models import Services, Faqs
from .serializers import ServiceSerializer, FaqsSerializer
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
