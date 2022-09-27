from django.contrib import admin
from .models import Faqs, Services


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
