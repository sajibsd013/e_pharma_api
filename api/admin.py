from django.contrib import admin
from .models import Doctors, Faqs, Appointments, CallDoctors, CallAppointments, Services


# Register your models here.


class ServicesAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = Services


admin.site.register(Services, ServicesAdmin)


class FaqsAdmin(admin.ModelAdmin):
    list_display = ["id", "ques", "ans"]

    class Meta:
        model = Faqs


admin.site.register(Faqs, FaqsAdmin)


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "address"]

    class Meta:
        model = Doctors


admin.site.register(Doctors, DoctorsAdmin)


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "patient_name", "patient_phone", "created_date"]

    class Meta:
        model = Appointments


admin.site.register(Appointments, AppointmentsAdmin)


class CallDoctorsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "address"]

    class Meta:
        model = CallDoctors


admin.site.register(CallDoctors, CallDoctorsAdmin)


class CallAppointmentsAdmin(admin.ModelAdmin):
    list_display = ["id", "patient_name", "patient_phone", "created_date"]

    class Meta:
        model = CallAppointments


admin.site.register(CallAppointments, CallAppointmentsAdmin)
