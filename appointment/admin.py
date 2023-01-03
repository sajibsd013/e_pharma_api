from django.contrib import admin
from .models import DoctorsAppointment , Medicine


class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient_name", "patient_phone", "doctor_id"]

    class Meta:
        model = DoctorsAppointment


admin.site.register(DoctorsAppointment,
                    DoctorAppointmentAdmin)

class MedicineAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "payment_status","service_status"]

    class Meta:
        model = Medicine


admin.site.register(Medicine,
                    MedicineAdmin)
