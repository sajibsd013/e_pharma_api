from .models import Blog, Comment
from .serializers import BlogSerializer, BlogSerializePOST, CommentSerializer, CommentSerializePOST
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET','Post'])
def blog_list(request):
    if request.method == 'GET':
        # blog = Blog.objects.all().order_by("created_date").reverse()
        # print(blog)
        if 'user' in request.GET:
            print(request.GET['user'])
            blog = Blog.objects.filter(
                user=request.GET['user']).order_by("-id")
        else:
            blog = Blog.objects.all().order_by("created_date").reverse()

        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BlogSerializePOST(data=request.data)
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


@api_view(['GET','Post'])
def comment_list(request):
    if request.method == 'GET':
        if 'blog' in request.GET:
            comment = Comment.objects.filter(
                blog=request.GET['blog']).order_by("-id")
            serializer = CommentSerializer(comment, many=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'POST':
        serializer = CommentSerializePOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(
            comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
