from rest_framework import serializers
from .models import DoctorsAppointment , Medicine


class DoctorsAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsAppointment
        fields = "__all__"

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"
