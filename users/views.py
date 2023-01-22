from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_tokens_for_user, isOtpMatcheed
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from .models import MyUser

from .serializers import RegistrationSerializer, PasswordChangeSerializer
from .custom_serializers import UserFullSerializer
# Create your views here.


class RegistrationView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        otp = request.data.get("otp")
        is_matched = isOtpMatcheed(phone, otp, "regi")
        if is_matched:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("OTP not matched!", status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        otp = request.data.get("otp")
        is_matched = isOtpMatcheed(phone, otp, "login")
        if is_matched:
            if 'phone' not in request.data:
                return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
            phone = request.data.get('phone')
            user = authenticate(request, username=phone, password="None")
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
            return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response("OTP not matched!", status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = PasswordChangeSerializer(
            context={'request': request}, data=request.data)
        # Another way to write is as in Line 17
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentLoggedInUser(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = UserFullSerializer

    def retrieve(self, request, *args, **kwargs):
        user_profile = self.queryset.get(phone=request.user.phone)
        serializer = self.get_serializer(user_profile)
        return Response({'user': serializer.data})


# @api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def UserDetail(request, pk):
    """
    Retrieve, update or delete a code  MyUser.
    """
    try:
        user = MyUser.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserFullSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserFullSerializer(
            user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
