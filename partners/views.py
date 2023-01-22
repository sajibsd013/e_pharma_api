from django.shortcuts import render
from .serializers import NurseSerializer, CareGiverSerializer, PhysiotherapistSerializer, PartnerSerializer, DoctorSerializer, DMF_DoctorSerializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.decorators import api_view
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
            serializer.save()
            msg = 'Dear doctor! Thank you very much for registering as a doctor at sasthosebok.com Take advantage of digitalization, serve more patients. Call if necessary +8801959970664'
            send_sms(mobile, msg)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        doctor = Doctor.objects.all().order_by('name').reverse()
        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def doctor_details(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)


@api_view(['POST'])
def dmf_doctor(request):
    if request.method == 'POST':
        serializer = DMF_DoctorSerializer(data=request.data)
        mobile = request.data.get("mobile")
        if serializer.is_valid():
            serializer.save()
            # send sms to admin and user
            # s1 = send_sms(
            #     mobile, "Registration Success, We will contact you soon")

            # if s1:
            #     send_sms("+8801959970664, +8801771147384",
            #              f"{mobile} Registered as a DMF/CP Doctor")
            #     serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def partner(request):
    if request.method == 'POST':
        serializer = PartnerSerializer(data=request.data)

        if serializer.is_valid():
            mobile = request.data.get("mobile")
            serializer.save()
            msg = 'সম্মানিত সেবক পার্টনার। sasthosebok.com এ রেজিস্ট্রেশনের জন্য আপনাকে ধন্যবাদ। ডিজিটাল যুগের সুযোগ নিন,আপনার ফার্মেসীর মাধ্যমে আরো বেশি সংখ্যক মানুষকে সেবা দিন।'
            send_sms(mobile, msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def care_giver(request):
    if request.method == 'POST':
        serializer = CareGiverSerializer(data=request.data)
        mobile = request.data.get("mobile")

        if serializer.is_valid():
            serializer.save()
            msg = 'sasthosebok.com এ CareGiver সার্ভিস নিবন্ধনের জন্য আপনাকে ধন্যবাদ। প্রয়োজনে কল করুন +8801959970664'
            send_sms(mobile, msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def physiotherapist(request):
    if request.method == 'POST':
        serializer = PhysiotherapistSerializer(data=request.data)
        mobile = request.data.get("mobile")

        if serializer.is_valid():
            serializer.save()
            msg = 'sasthosebok.com এ ফিজিওথেরাপিস্ট সার্ভিস নিবন্ধনের জন্য আপনাকে ধন্যবাদ। প্রয়োজনে কল করুন +8801959970664'
            send_sms(mobile, msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def nurse_regi(request):
    if request.method == 'POST':
        serializer = NurseSerializer(data=request.data)
        mobile = request.data.get("mobile")

        if serializer.is_valid():
            serializer.save()
            msg = 'sasthosebok.com এ হোম-নার্সিং/মিডওয়াইফারি সার্ভিস নিবন্ধনের জন্য আপনাকে ধন্যবাদ। প্রয়োজনে কল করুন +8801959970664'
            send_sms(mobile, msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
