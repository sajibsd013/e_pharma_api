from django.contrib import admin
from .models import Job


# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "depertment"]

    class Meta:
        model = Job


admin.site.register(Job, JobAdmin)

