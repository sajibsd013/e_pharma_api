from rest_framework import serializers
from .models import Diagnostic, HomeMedicine, DeviceCircumcision



class HomeMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeMedicine
        fields = "__all__"

class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = "__all__"

class DeviceCircumcisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCircumcision
        fields = "__all__"
