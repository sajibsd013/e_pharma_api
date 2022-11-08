from django.shortcuts import render
from .serializers import NurseSerializer, CareGiverSerializer, PhysiotherapistSerializer, PartnerSerializer, DoctorSerializer, DMF_DoctorSerializer
from rest_framework import viewsets, pagination
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from api.utils import send_sms
from rest_framework.views import APIView
from .models import Doctor
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctotList(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            mobile = request.data.get("mobile")
            s1 = send_sms(
                mobile, "Registration Success, We will contact you soon")

            if s1:
                send_sms("+8801959970664, +8801771147384",
                         f"{mobile} Registered as a Doctor")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def dmf_doctor(request):
    if request.method == 'POST':
        serializer = DMF_DoctorSerializer(data=request.data)
        mobile = request.data.get("mobile")
        if serializer.is_valid():
            # send sms to admin and user
            s1 = send_sms(
                mobile, "Registration Success, We will contact you soon")

            if s1:
                send_sms("+8801959970664, +8801771147384",
                         f"{mobile} Registered as a DMF/CP Doctor")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @parser_classes([MultiPartParser, ])
# def doctor(request):
#     if request.method == 'POST':
#         serializer = DoctorSerializer(data=request.data)
#         mobile = request.data.get("mobile")
#         if serializer.is_valid():
#             # send sms to admin and user
#             # send_sms(mobile, "Registration Success, We will contact you soon")
#             # send_sms("+8801959970664, +8801771147384",
#             #          f"{mobile} Registered as a Doctor")
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def partner(request):
    if request.method == 'POST':
        serializer = PartnerSerializer(data=request.data)
        mobile = request.data.get("mobile")

        if serializer.is_valid():

            s1 = send_sms(
                mobile, "Registration Success, We will contact you soon")

            if s1:
                send_sms("+8801959970664, +8801771147384",
                         f"{mobile} Registered as a partner")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def care_giver(request):
    if request.method == 'POST':
        serializer = CareGiverSerializer(data=request.data)
        mobile = request.data.get("mobile")

        if serializer.is_valid():

            s1 = send_sms(
                mobile, "Registration Success, We will contact you soon")

            if s1:
                send_sms("+8801959970664, +8801771147384",
                         f"{mobile} Registered as a caregiver")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def physiotherapist(request):
    if request.method == 'POST':
        serializer = PhysiotherapistSerializer(data=request.data)
        mobile = request.data.get("mobile")

        if serializer.is_valid():
            # send sms to admin and user
            s1 = send_sms(
                mobile, "Registration Success, We will contact you soon")

            if s1:
                send_sms("+8801959970664, +8801771147384",
                         f"{mobile} Registered as a physiotherapist")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def nurse_regi(request):
    if request.method == 'POST':
        serializer = NurseSerializer(data=request.data)
        mobile = request.data.get("mobile")

        if serializer.is_valid():
            s1 = send_sms(
                mobile, "Registration Success, We will contact you soon")

            if s1:
                send_sms("+8801959970664, +8801771147384",
                         f"{mobile} Registered as a Nurse/Midwife")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
