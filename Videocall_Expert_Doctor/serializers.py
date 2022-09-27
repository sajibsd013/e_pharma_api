from rest_framework import serializers
from .models import VideoCallExpertDoctor, VideoCallExpertDoctorsAppointment


class VideoCallExpertDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCallExpertDoctor
        fields = "__all__"


class VideoCallExpertsAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCallExpertDoctorsAppointment
        fields = "__all__"
