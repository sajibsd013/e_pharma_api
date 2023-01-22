from django.db import models
from django.utils.timezone import now
from users.models import MyUser

# Create your models here.
STATUS_CHOICES = (
    ('pending', 'pending'),
    ('cancelled', 'cancelled'),
    ('completed', 'completed'),
    ('approved', 'approved'),
)
PAYMENT_CHOICES = (
    ('unpaid', 'unpaid'),
    ('pending', 'pending'),
    ('paid', 'paid'),
)
PAYMENT_METHOD = (
    ('Bkash', 'Bkash'),
    ('Nogod', 'Nogod'),
    ('Rocket', 'Rocket'),
    ('Upay', 'Upay'),
)


def upload_to_diagnostic(instance, filename):
    return 'images/diagnostic/{filename}'.format(filename=filename)

class Diagnostic(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    fee = models.CharField(max_length=120, null=True, blank=True, default="")
    user = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True, related_name='diagnostic')
    image_url = models.ImageField(
        upload_to=upload_to_diagnostic, null=True, blank=True)
    created_date = models.DateTimeField(default=now, editable=False)
    payment_method = models.CharField(
        max_length=120, choices=PAYMENT_METHOD, default="Bkash", )
    transaction_id = models.CharField(max_length=120, null=True, blank=True, default="")
    payment_status = models.CharField(
        max_length=120, choices=PAYMENT_CHOICES, default="unpaid", )
    service_status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending", )
    address = models.TextField()

    class Meta:
        verbose_name_plural = "Mobile Diagnostic"



def upload_to_medicine(instance, filename):
    return 'images/medicine/{filename}'.format(filename=filename)

class HomeMedicine(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    fee = models.CharField(max_length=120, null=True, blank=True, default="")
    user = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True, related_name='medicine')
    image_url = models.ImageField(
        upload_to=upload_to_medicine, null=True, blank=True)
    created_date = models.DateTimeField(default=now, editable=False)
    payment_method = models.CharField(
        max_length=120, choices=PAYMENT_METHOD, default="Bkash", )
    transaction_id = models.CharField(max_length=120, null=True, blank=True, default="")
    payment_status = models.CharField(
        max_length=120, choices=PAYMENT_CHOICES, default="unpaid", )
    service_status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending", )
    medicine = models.TextField()
    address = models.TextField()

    class Meta:
        verbose_name_plural = "Home Medicine"
