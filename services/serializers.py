from rest_framework import serializers
from .models import  Diagnostic , HomeMedicine



class HomeMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeMedicine
        fields = "__all__"

class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = "__all__"
