from rest_framework import serializers
from .models import *


class DoctorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInfo
        fields = "__all__"

class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = "__all__"

class ChiefComplaientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiefComplaient
        fields = "__all__"

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

class ExaminationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examinations
        fields = "__all__"

class DiagosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagosis
        fields = "__all__"

class InvestigationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investigations
        fields = "__all__"


class AdvicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advices
        fields = "__all__"


class FollowupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followup
        fields = "__all__"

