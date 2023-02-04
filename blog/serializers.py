from rest_framework import serializers
from .models import Blog, Comment
from users.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = "__all__"

    def get_user(self, obj):
        return UserSerializer(obj.user).data


class BlogSerializePOST(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"




class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_user(self, obj):
        return UserSerializer(obj.user).data


class CommentSerializePOST(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"





