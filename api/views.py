from django.shortcuts import render
from .models import Services, Faqs
from .serializers import ServiceSerializer, FaqsSerializer, OtpSerializer
from rest_framework import viewsets, pagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import send_otp_checker, send_sms, send_otp
from random import randrange
from .models import OTP
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


# @custom_view_decorator


@api_view(['POST'])
def set_otp(request):
    if request.method == 'POST':
        phone = request.data.get("phone")
        type = request.data.get("type")

        otp = randrange(1000, 9999)
        check = send_otp_checker(phone, type)

        if check["c_type"]:
            try:
                otp_dict = OTP.objects.filter(phone=phone).update(otp=otp)
                if otp_dict:
                    # send otp
                    # send_otp(phone, otp)
                    return Response("success", status=status.HTTP_201_CREATED)
                else:
                    serializer = OtpSerializer(
                        data={"phone": phone, "otp": otp})
                    if serializer.is_valid():
                        # send otp
                        # send_otp(phone, otp)

                        serializer.save()
                        return Response("success", status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except:
                return Response("Unknown Error!", status=status.HTTP_400_BAD_REQUEST)
        return Response(check['msg'], status=status.HTTP_400_BAD_REQUEST)
