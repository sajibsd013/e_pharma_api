from email.policy import default
from django.db import models
from django.utils.timezone import now
from users.models import MyUser

# Create your models here.

STATUS_CHOICES = (
    ('pending', 'pending'),
    ('approved', 'approved'),
)
GENDER = (
    ('male', 'male'),
    ('female', 'female'),
    ('others', 'others'),
)

# lets us explicitly set upload path and filename


def upload_to_doctor(instance, filename):
    return 'images/doctor/{filename}'.format(filename=filename)


class DMF_Doctor(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120, unique=True)
    nid = models.CharField(max_length=120, unique=True, null=True)
    qualicifacions = models.CharField(max_length=120)
    specialty = models.CharField(max_length=120)
    bmdc_regi_no = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    working_area = models.CharField(
        max_length=120, null=True, blank=True)
    working_days = models.CharField(max_length=120)
    working_times = models.CharField(max_length=120)
    working_times = models.CharField(max_length=120)
    payment_method = models.CharField(max_length=120, null=True)
    payment_number = models.CharField(max_length=120, null=True)
    status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending", )
    image_url = models.ImageField(
        upload_to=upload_to_doctor, blank=True, null=True)
    experience = models.TextField()

    institution_or_chamber_address = models.TextField(
        null=True, blank=True)
    short_description = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Home call/Video Call DMF/CCP Doctors List"


def upload_to_doctor(instance, filename):
    return 'images/doctor/{filename}'.format(filename=filename)


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120, unique=True)
    nid = models.CharField(max_length=120, unique=True, null=True)
    qualicifacions = models.CharField(max_length=120)
    specialty = models.CharField(max_length=120)
    bmdc_regi_no = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    city = models.CharField(
        max_length=120, null=True, blank=True, )
    working_area = models.CharField(
        max_length=500, null=True, blank=True, )
    working_days = models.CharField(max_length=120)
    working_times = models.CharField(max_length=120)
    gender = models.CharField(
        max_length=120, choices=GENDER, null=True)
    payment_method = models.CharField(max_length=120, null=True)
    payment_number = models.CharField(max_length=120, null=True)
    status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending", )
    image_url = models.ImageField(
        upload_to=upload_to_doctor, null=True)
    experience = models.TextField()
    institution_or_chamber_address = models.TextField(
        null=True, blank=True, )
    short_description = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Home call/Video Call Doctors List"


def upload_to_partner(instance, filename):
    return 'images/partner/{filename}'.format(filename=filename)


class Partner(models.Model):
    pharmacy_name = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120, unique=True)
    service_provider_name = models.CharField(max_length=120, null=True,)
    service_provider_mobile = models.CharField(max_length=120, null=True)
    nid = models.CharField(max_length=120, unique=True, null=True)
    tred_licence = models.CharField(max_length=120, unique=True, null=True)
    working_area = models.CharField(max_length=120)
    status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending")
    image_url = models.ImageField(
        upload_to=upload_to_partner, blank=True, null=True)
    short_description = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Partners (pharmacy) List"


# lets us explicitly set upload path and filename
def upload_to_caregiver(instance, filename):
    return 'images/caregiver/{filename}'.format(filename=filename)


class CareGiver(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120, unique=True)
    nid = models.CharField(max_length=120, unique=True, null=True)
    working_area = models.CharField(max_length=120)
    working_days = models.CharField(max_length=120)
    qualicifacions = models.CharField(max_length=120, null=True)
    status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending")
    gender = models.CharField(
        max_length=120, choices=GENDER, null=True)
    image_url = models.ImageField(
        upload_to=upload_to_caregiver, blank=True, null=True)
    institution = models.TextField(
        null=True, blank=True, )
    short_description = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Caregivers List"

# lets us explicitly set upload path and filename


def upload_to_nurse(instance, filename):
    return 'images/nurse/{filename}'.format(filename=filename)


class Nurse(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120, unique=True)
    nid = models.CharField(max_length=120, unique=True, null=True)
    qualicifacions = models.CharField(max_length=120)
    working_area = models.CharField(max_length=120)
    working_days = models.CharField(max_length=120)
    working_times = models.CharField(max_length=120)
    institution = models.TextField(
        null=True, blank=True, )
    status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending")
    gender = models.CharField(
        max_length=120, choices=GENDER, null=True)

    image_url = models.ImageField(
        upload_to=upload_to_nurse, blank=True, null=True)
    short_description = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Nurse List"

# lets us explicitly set upload path and filename


def upload_to_physiotherapist(instance, filename):
    return 'images/physiotherapist/{filename}'.format(filename=filename)


class Physiotherapist(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120, unique=True)
    nid = models.CharField(max_length=120, unique=True, null=True)
    qualicifacions = models.CharField(max_length=120)
    institution = models.CharField(max_length=120, null=True)
    working_area = models.CharField(max_length=120)
    working_days = models.CharField(max_length=120)
    working_times = models.CharField(max_length=120)
    status = models.CharField(
        max_length=120, choices=STATUS_CHOICES, default="pending")

    image_url = models.ImageField(
        upload_to=upload_to_physiotherapist, blank=True, null=True)
    short_description = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Physiotherapist List"
