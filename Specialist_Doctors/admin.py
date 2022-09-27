from django.contrib import admin
from .models import SpecialistDoctor, SpecialistDoctorsAppointment


# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "speciality", "address"]

    class Meta:
        model = SpecialistDoctor


admin.site.register(SpecialistDoctor, DoctorAdmin)


class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display = ["id", "patient_name", "patient_phone", "doctor_id"]

    class Meta:
        model = SpecialistDoctorsAppointment


admin.site.register(SpecialistDoctorsAppointment,
                    DoctorAppointmentAdmin)
