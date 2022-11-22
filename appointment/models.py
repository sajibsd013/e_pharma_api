from django.db import models
from django.utils.timezone import now
from partners.models import Doctor
from users.models import MyUser

# Create your models here.
STATUS_CHOICES = (
    ('pending', 'pending'),
    ('approved', 'approved'),
)
PAYMENT_CHOICES = (
    ('pending', 'pending'),
    ('paid', 'paid'),
)
PAYMENT_METHOD = (
    ('Bkash', 'Bkash'),
    ('Nogod', 'Nogod'),
    ('Rocket', 'Rocket'),
    ('Upay', 'Upay'),
)


class DoctorsAppointment(models.Model):
    patient_name = models.CharField(max_length=120)
    patient_age = models.CharField(max_length=120)
    patient_phone = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    fee = models.CharField(max_length=120)
    doctor_id = models.ForeignKey(
        Doctor, verbose_name="Doctor", on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    created_date = models.DateTimeField(default=now, editable=False)
    payment_method = models.CharField(
        max_length=120, choices=PAYMENT_METHOD, default="Bkash", )
    transaction_id = models.CharField(max_length=120, null=True, blank=True)
    payment_status = models.CharField(
        max_length=120, choices=PAYMENT_CHOICES, default="pending", )
    service_status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending", )
    details = models.TextField()

    class Meta:
        verbose_name_plural = "Doctors Appointment"
