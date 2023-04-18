from django.shortcuts import render
from .models import Product, Order, Medicine
from .serializers import ProductSerializer ,OrderSerializer, MedicineSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from api.utils import send_admin_notifications

# Create your views here.




@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def Orders(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = "Please confirm Order"
            send_admin_notifications(msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if 'user_id' in request.GET:
            print(request.GET['user_id'])
            services = Order.objects.filter(
                user_id=request.GET['user_id']).order_by("-id")

        else:
            services = Order.objects.all()
        serializer = OrderSerializer(services, many=True)

        return Response(serializer.data)


@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def OrdersDetails(request, pk):
    """
    Retrieve, update or delete a code  .
    """
    try:
        order_0 = Order.objects.get(pk=pk)
    except order_0.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order_0)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(
            order_0, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_0.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def medicine_list(request):
    if request.method == 'GET':
        data = Medicine.objects.all()
        serializer = MedicineSerializer(data, many=True)
        return Response(serializer.data)

