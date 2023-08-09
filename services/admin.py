from django.contrib import admin
from .models import Diagnostic , HomeMedicine, DeviceCircumcision


class HomeMedicineAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "payment_status","service_status"]

    class Meta:
        model = HomeMedicine


admin.site.register(HomeMedicine,
                    HomeMedicineAdmin)

class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "payment_status","service_status"]

    class Meta:
        model = Diagnostic


admin.site.register(Diagnostic,
                    DiagnosticAdmin)

class DeviceCircumcisionAdmin(admin.ModelAdmin):
    list_display = ["child_name", "phone", "address"]

    class Meta:
        model = DeviceCircumcision


admin.site.register(DeviceCircumcision,
                    DeviceCircumcisionAdmin)
