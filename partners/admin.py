from warnings import filters
from django.contrib import admin
from .models import Nurse, CareGiver, Physiotherapist, Partner, Doctor, DMF_Doctor


# Register your models here.


class DMF_DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "specialty", "type", "mobile", "status"]
    search_fields = ("name", "working_area", "status")
    list_filter = ("working_area", "specialty", "type", "status")

    class Meta:
        model = DMF_Doctor


admin.site.register(DMF_Doctor, DMF_DoctorAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "specialty", "type", "mobile", "status"]
    search_fields = ("name", "working_area", "status")
    list_filter = ("working_area", "specialty", "type", "status")

    class Meta:
        model = Doctor


admin.site.register(Doctor, DoctorAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ["name", "working_area", "status"]
    search_fields = ("name", "working_area", "status")
    list_filter = ("working_area",
                   "status")

    class Meta:
        model = Partner


admin.site.register(Partner, PartnerAdmin)


class CareGiverAdmin(admin.ModelAdmin):
    list_display = ["name", "working_area",
                    "working_days", "status"]
    search_fields = ("name", "working_area", "working_days", "status")
    list_filter = ("working_area",
                   "status")

    class Meta:
        model = CareGiver


admin.site.register(CareGiver, CareGiverAdmin)


class PhysiotherapistAdmin(admin.ModelAdmin):
    list_display = ["name", "working_area",
                    "working_days", "working_times", "status"]
    search_fields = ("name", "working_area", "working_days",
                     "working_times", "status")
    # filter_horizontal = ("status",)
    list_filter = ("working_area",
                   "status")

    class Meta:
        model = Physiotherapist


admin.site.register(Physiotherapist, PhysiotherapistAdmin)


class NurseAdmin(admin.ModelAdmin):
    list_display = ["name", "working_area",
                    "working_days", "working_times", "status"]
    search_fields = ("name", "working_area", "working_days",
                     "working_times", "status")
    # filter_horizontal = ("status",)
    list_filter = ("working_area",
                   "status")

    class Meta:
        model = Nurse


admin.site.register(Nurse, NurseAdmin)
