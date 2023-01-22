from django.contrib import admin
from .models import DoctorsAppointment 


class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient_name", "patient_phone"]

    class Meta:
        model = DoctorsAppointment


admin.site.register(DoctorsAppointment,
                    DoctorAppointmentAdmin)


