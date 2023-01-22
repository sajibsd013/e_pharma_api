from rest_framework import serializers
from .models import * 


class DoctorsAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsAppointment
        fields = "__all__"
