from rest_framework import serializers
from .models import Services, Faqs, OTP, SMS_TOKEN, GenaralInformation , Speciality , BmiFaqs,JournalGuidelines


class JournalGuidelinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalGuidelines
        fields = "__all__"

class GenaralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenaralInformation
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = "__all__"

class BmiFaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmiFaqs
        fields = "__all__"

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = "__all__"


class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = "__all__"


class SmsTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS_TOKEN
        fields = "__all__"
