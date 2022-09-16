from django.db import models
from django.utils.timezone import now

# Create your models here.


# lets us explicitly set upload path and filename
def upload_to_services(instance, filename):
    return 'images/doctors/{filename}'.format(filename=filename)


class Services(models.Model):
    title = models.CharField(max_length=120)
    image_url = models.ImageField(
        upload_to=upload_to_services, blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Services List"
        db_table = "Services"


class Faqs(models.Model):
    ques = models.CharField(max_length=120)
    ans = models.TextField()

    class Meta:
        verbose_name_plural = "FAGs List"
        db_table = "Faqs"


# lets us explicitly set upload path and filename
def upload_to_doctors(instance, filename):
    return 'images/doctors/{filename}'.format(filename=filename)


class Doctors(models.Model):
    name = models.CharField(max_length=120)
    qualifications = models.TextField(null=True)
    expericence = models.TextField(null=True)
    address = models.TextField(null=True)
    time = models.TextField(null=True)
    image_url = models.ImageField(
        upload_to=upload_to_doctors, blank=True, null=True)
    category = models.CharField(max_length=100, null=True)
    fee = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Doctors List"
        db_table = "Doctors"


class Appointments(models.Model):
    patient_name = models.CharField(max_length=120)
    patient_age = models.CharField(max_length=120)
    patient_phone = models.CharField(max_length=120)
    details = models.TextField()
    doctor_id = models.ForeignKey(
        Doctors, verbose_name="Doctor ID", on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Appointments List"
        db_table = "Appointments"


# lets us explicitly set upload path and filename
def upload_to_call_doctors(instance, filename):
    return 'images/call-doctors/{filename}'.format(filename=filename)


class CallDoctors(models.Model):
    name = models.CharField(max_length=120)
    qualifications = models.TextField(null=True)
    expericence = models.TextField(null=True)
    address = models.TextField(null=True)
    time = models.TextField(null=True)
    image_url = models.ImageField(
        upload_to=upload_to_call_doctors, blank=True, null=True)
    category = models.CharField(max_length=100, null=True)
    fee = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Call Doctors List"
        db_table = "Call_Doctors"


class CallAppointments(models.Model):
    patient_name = models.CharField(max_length=120)
    patient_age = models.CharField(max_length=120)
    patient_phone = models.CharField(max_length=120)
    details = models.TextField()
    doctor_id = models.ForeignKey(
        CallDoctors, verbose_name="Doctor ID", on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Call Appointments List"
        db_table = "CallAppointments"
