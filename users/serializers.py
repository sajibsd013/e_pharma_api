from rest_framework import serializers
from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['phone', 'full_name']

    def save(self):
        user = MyUser(
            phone=self.validated_data['phone'], full_name=self.validated_data['full_name'])

        user.set_password("None")
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(
        style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(
                {'current_password': 'Does not match'})
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"

