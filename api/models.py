from django.db import models
from django.utils.timezone import now
from users.models import MyUser

# Create your models here.


# lets us explicitly set upload path and filename
def upload_to_services(instance, filename):
    return 'images/services/{filename}'.format(filename=filename)


class Services(models.Model):
    title = models.CharField(max_length=120)
    path = models.CharField(max_length=120, blank=True, null=True)
    image_url = models.ImageField(
        upload_to=upload_to_services, blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Services"
        db_table = "Services"

class Faqs(models.Model):
    ques = models.CharField(max_length=120)
    ans = models.TextField()

    class Meta:
        verbose_name_plural = "FAQs "
        db_table = "Faqs"

class BmiFaqs(models.Model):
    ques = models.CharField(max_length=120)
    ans = models.TextField()

    class Meta:
        verbose_name_plural = "BMI FAQs "
        db_table = "BmiFaqs"


class Speciality(models.Model):
    speciality = models.CharField(max_length=120)
    class Meta:
        verbose_name_plural = "Doctors Speciality "


class OTP(models.Model):
    phone = models.CharField(max_length=120, unique=True)
    otp = models.CharField(max_length=120)
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "OTP "
        db_table = "OTP"


class SMS_TOKEN(models.Model):
    token = models.CharField(max_length=220)
    status = models.CharField(max_length=120)
    api_url = models.CharField(max_length=220, null=True)

    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "SMS TOKEN "
        db_table = "SMS_TOKEN"


class GenaralInformation(models.Model):
    name = models.CharField(max_length=220)
    address = models.CharField(max_length=220)
    email = models.CharField(max_length=220)
    phone_1 = models.CharField(max_length=16)
    phone_2 = models.CharField(max_length=16)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Genaral Information"
        db_table = "GenaralInformation"
