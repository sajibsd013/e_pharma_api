from django.contrib import admin
from .models import DoctorsAppointment


class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient_name", "patient_phone", "doctor_id"]

    class Meta:
        model = DoctorsAppointment


admin.site.register(DoctorsAppointment,
                    DoctorAppointmentAdmin)
