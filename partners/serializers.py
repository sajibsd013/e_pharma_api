from rest_framework import serializers
from .models import Nurse, CareGiver, Physiotherapist, Partner, Doctor, DMF_Doctor


class DMF_DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DMF_Doctor
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class PhysiotherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physiotherapist
        fields = "__all__"


class CareGiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareGiver
        fields = "__all__"


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = "__all__"
