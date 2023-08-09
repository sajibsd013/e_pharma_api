from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Diagnostic, HomeMedicine, DeviceCircumcision
from .serializers import  DiagnosticSerializer, HomeMedicineSerializer, DeviceCircumcisionSerializer
from api.utils import send_admin_notifications, send_sms
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# @custom_view_decorator




@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def Medicine(request):
    if request.method == 'POST':
        serializer = HomeMedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = "Please confirm Home Medicine Services"
            send_admin_notifications(msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if 'user_id' in request.GET:
            print(request.GET['user_id'])
            services = HomeMedicine.objects.filter(
                user_id=request.GET['user_id']).order_by("-id")

        else:
            services = HomeMedicine.objects.all()
        serializer = HomeMedicineSerializer(services, many=True)

        return Response(serializer.data)



@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def MedicineDetails(request, pk):
    """
    Retrieve, update or delete a code  DoctorsAppointment.
    """
    try:
        Home_Meedicine = HomeMedicine.objects.get(pk=pk)
    except Home_Meedicine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HomeMedicineSerializer(Home_Meedicine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HomeMedicineSerializer(
            Home_Meedicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Home_Meedicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def MobileDiagnostic(request):
    if request.method == 'POST':
        serializer = DiagnosticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = "Please confirm Home Diagnostic Services"
            send_admin_notifications(msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if 'user' in request.GET:
            print(request.GET['user'])
            services = Diagnostic.objects.filter(
                user=request.GET['user']).order_by("-id")

        else:
            services = Diagnostic.objects.all()
        serializer = DiagnosticSerializer(services, many=True)

        return Response(serializer.data)



@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def MobileDiagnosticDetails(request, pk):
    """
    Retrieve, update or delete a code  MobileDiagnosticDetails.
    """
    try:
        Mobile_Diagnostic = Diagnostic.objects.get(pk=pk)
    except Mobile_Diagnostic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiagnosticSerializer(Mobile_Diagnostic)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiagnosticSerializer(
            Mobile_Diagnostic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Mobile_Diagnostic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def MobileDeviceCircumcision(request):
    if request.method == 'POST':
        serializer = DeviceCircumcisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = "Please confirm Device Circumcision Services"
            send_admin_notifications(msg)
            msg_to_user = "ধন্যবাদ প্রিয় গ্রাহক আপনার আবেদনটি সাদরে গ্রহণ করা হলো স্বাস্থ্যসেবক ডট কম।"
            to = request.data['phone']
            send_sms(to, msg_to_user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if 'user' in request.GET:
            print(request.GET['user'])
            services = DeviceCircumcision.objects.filter(
                user=request.GET['user']).order_by("-id")

        else:
            services = DeviceCircumcision.objects.all()
        serializer = DiagnosticSerializer(services, many=True)

        return Response(serializer.data)



@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def MobileDeviceCircumcisionDetails(request, pk):
    """
    Retrieve, update or delete a code  MobileDiagnosticDetails.
    """
    try:
        Device_Circumcision = DeviceCircumcision.objects.get(pk=pk)
    except Device_Circumcision.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeviceCircumcisionSerializer(Device_Circumcision)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeviceCircumcisionSerializer(
            Device_Circumcision, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Device_Circumcision.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

