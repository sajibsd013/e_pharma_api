from django.contrib import admin
from .models import Faqs, Services, OTP, SMS_TOKEN


# Register your models here.


class SMS_TOKENAdmin(admin.ModelAdmin):
    list_display = ["id", "token", "status", "api_url", "created_date"]

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


class FaqsAdmin(admin.ModelAdmin):
    list_display = ["id", "ques", "ans"]

    class Meta:
        model = Faqs


admin.site.register(Faqs, FaqsAdmin)
