from warnings import filters
from django.contrib import admin
from .models import  *


# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "total_cost", "payment_status","get_products","created_date"]
    # list_display = [field.name for field in Order._meta.fields if field.name != "id"]
    list_filter = ("payment_status","service_status",)

    def get_products(self, obj):
        return "\n".join([f'{p.id} -{p.name} - ({p.category})' for p in obj.products.all()])

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price","quantity","offer"]
    # list_display = [field.name for field in Product._meta.fields if field.name != "id"]
    list_filter = ("category",)

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
