from django.contrib import admin
from .models import Diagnostic , HomeMedicine


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
