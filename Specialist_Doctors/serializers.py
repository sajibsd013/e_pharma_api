from rest_framework import serializers
from .models import SpecialistDoctor, SpecialistDoctorsAppointment


class SpecialistDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistDoctor
        fields = "__all__"


class SpecialistDoctorsAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistDoctorsAppointment
        fields = "__all__"
