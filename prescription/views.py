from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Create your views here.

@api_view(['POST', 'GET'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JWTAuthentication,))
def doctor_info(request):
    if request.method == 'POST':
        serializer = DoctorInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if 'user_id' in request.GET:
            services = DoctorInfo.objects.filter(
                user_id=request.GET['user_id']).order_by("-id")

            serializer = DoctorInfoSerializer(services, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


       
@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def doctor_info_detail(request, pk):
    """
    Retrieve, update or delete a code  doctor.
    """
    try:
        doctor = DoctorInfo.objects.get(pk=pk)
    except doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorInfoSerializer(doctor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DoctorInfoSerializer(
            doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JWTAuthentication,))
def prescriptions(request):
    if request.method == 'POST':
        serializer = PrescriptionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if 'user_id' in request.GET:
            services = Prescriptions.objects.filter(
                user_id=request.GET['user_id']).order_by("-id")

            serializer = PrescriptionsSerializer(services, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
       
@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def prescriptions_detail(request, pk):
    """
    Retrieve, update or delete a code  Prescriptions.
    """
    try:
        Prescription = Prescriptions.objects.get(pk=pk)
    except Prescription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PrescriptionsSerializer(Prescription)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PrescriptionsSerializer(
            Prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Prescription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_prescription_data(request):
    if request.method == 'GET':
        chief_complaient_data = ChiefComplaient.objects.all()
        chief_complaient_serializer = ChiefComplaientSerializer(
            chief_complaient_data, many=True)

        history_data = History.objects.all()
        history_serializer = HistorySerializer(history_data, many=True)

        examinations_data = Examinations.objects.all()
        examinations_serializer = ExaminationsSerializer(
            examinations_data, many=True)

        diagosis_data = Diagosis.objects.all()
        diagosis_serializer = DiagosisSerializer(diagosis_data, many=True)

        advices_data = Advices.objects.all()
        advices_serializer = AdvicesSerializer(advices_data, many=True)

        followup_data = Followup.objects.all()
        followup_serializer = FollowupSerializer(followup_data, many=True)

        investigations_data = Investigations.objects.all()
        investigations_serializer = InvestigationsSerializer(investigations_data, many=True)

        return Response({
            "chief_complaient": chief_complaient_serializer.data,
            "history": history_serializer.data,
            "examinations": examinations_serializer.data,
            "diagosis": diagosis_serializer.data,
            "advices": advices_serializer.data,
            "followup": followup_serializer.data,
            "investigations": investigations_serializer.data,
        })
