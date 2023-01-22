from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import randrange
# Create your views here.


@api_view(['GET','Post'])
def blog_list(request):
    if request.method == 'GET':
        blog = Blog.objects.select_related().order_by("created_date").reverse()
        print(blog)
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogSerializer(
            blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
