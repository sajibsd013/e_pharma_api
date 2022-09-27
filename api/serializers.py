from rest_framework import serializers
from .models import Services, Faqs


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = "__all__"
