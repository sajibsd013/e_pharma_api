from rest_framework import serializers
from .models import DoctorsAppointment


class DoctorsAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsAppointment
        fields = "__all__"
