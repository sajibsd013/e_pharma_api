from rest_framework import serializers
from .models import Services, Faqs, OTP, SMS_TOKEN


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = "__all__"


class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = "__all__"


class SmsTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS_TOKEN
        fields = "__all__"
