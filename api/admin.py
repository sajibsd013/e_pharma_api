from django.contrib import admin
from .models import Faqs, Services, OTP, SMS_TOKEN, GenaralInformation, Speciality , BmiFaqs


# Register your models here.


class GenaralInformationAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "email",
                    "phone_1", "phone_2", "description"]

    class Meta:
        model = GenaralInformation


admin.site.register(GenaralInformation, GenaralInformationAdmin)


class SMS_TOKENAdmin(admin.ModelAdmin):
    list_display = ["token", "status", "api_url", "created_date"]

    class Meta:
        model = SMS_TOKEN


admin.site.register(SMS_TOKEN, SMS_TOKENAdmin)


class OTPAdmin(admin.ModelAdmin):
    list_display = ["phone", "otp", "created_date"]

    class Meta:
        model = OTP


admin.site.register(OTP, OTPAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = Services


admin.site.register(Services, ServicesAdmin)

class SpecialityAdmin(admin.ModelAdmin):
    list_display = ["speciality"]

    class Meta:
        model = Speciality
admin.site.register(Speciality, SpecialityAdmin)

class FaqsAdmin(admin.ModelAdmin):
    list_display = ["ques", "ans"]

    class Meta:
        model = Faqs

admin.site.register(Faqs, FaqsAdmin)

class BmiFaqsAdmin(admin.ModelAdmin):
    list_display = ["ques", "ans"]

    class Meta:
        model = BmiFaqs

admin.site.register(BmiFaqs, BmiFaqsAdmin)



