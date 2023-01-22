from rest_framework import serializers
from .models import Blog
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





