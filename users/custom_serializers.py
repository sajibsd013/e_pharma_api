from rest_framework import serializers
from .models import MyUser
from appointment.serializers import DoctorsAppointmentSerializer
from services.serializers import HomeMedicineSerializer, DiagnosticSerializer

from blog.serializers import BlogSerializer

class UserFullSerializer(serializers.ModelSerializer):
    diagnostic = DiagnosticSerializer(many=True, read_only=True)
    medicine = HomeMedicineSerializer(many=True, read_only=True)
    appointment = DoctorsAppointmentSerializer(many=True, read_only=True)
    blog = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = MyUser
        fields = "__all__"

