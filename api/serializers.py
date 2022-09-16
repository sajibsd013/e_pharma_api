from rest_framework import serializers
from .models import Doctors, Services, Faqs, Appointments, CallDoctors, CallAppointments


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"


class CallDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallDoctors
        fields = "__all__"


class CallAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallAppointments
        fields = "__all__"
