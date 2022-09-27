from django.contrib import admin
from .models import VideoCallExpertDoctor, VideoCallExpertDoctorsAppointment


# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "speciality", "address"]

    class Meta:
        model = VideoCallExpertDoctor


admin.site.register(VideoCallExpertDoctor, DoctorAdmin)


class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display = ["id", "patient_name", "patient_phone", "doctor_id"]

    class Meta:
        model = VideoCallExpertDoctorsAppointment


admin.site.register(VideoCallExpertDoctorsAppointment,
                    DoctorAppointmentAdmin)
