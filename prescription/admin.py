from django.contrib import admin
from .models import *


# Register your models here.

class DoctorInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DoctorInfo._meta.fields if field.name != "id"]
    class Meta:
        model = DoctorInfo
admin.site.register(DoctorInfo, DoctorInfoAdmin)

class PrescriptionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Prescriptions._meta.fields if field.name != "id"]
    class Meta:
        model = Prescriptions
admin.site.register(Prescriptions, PrescriptionsAdmin)

class ChiefComplaientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ChiefComplaient._meta.fields if field.name != "id"]
    class Meta:
        model = ChiefComplaient
admin.site.register(ChiefComplaient, ChiefComplaientAdmin)

class HistoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in History._meta.fields if field.name != "id"]
    class Meta:
        model = History
admin.site.register(History, HistoryAdmin)

class ExaminationsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Examinations._meta.fields if field.name != "id"]
    class Meta:
        model = Examinations
admin.site.register(Examinations, ExaminationsAdmin)

class DiagosisAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Diagosis._meta.fields if field.name != "id"]
    class Meta:
        model = Diagosis
admin.site.register(Diagosis, DiagosisAdmin)

class InvestigationsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Investigations._meta.fields if field.name != "id"]
    class Meta:
        model = Investigations
admin.site.register(Investigations, InvestigationsAdmin)

class AdvicesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Advices._meta.fields if field.name != "id"]
    class Meta:
        model = Advices
admin.site.register(Advices, AdvicesAdmin)

class FollowupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Followup._meta.fields if field.name != "id"]
    class Meta:
        model = Followup
admin.site.register(Followup, FollowupAdmin)