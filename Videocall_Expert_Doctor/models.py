from django.db import models
from django.utils.timezone import now

# Create your models here.


# lets us explicitly set upload path and filename
def upload_to_doctors(instance, filename):
    return 'images/doctors/{filename}'.format(filename=filename)


class VideoCallExpertDoctor(models.Model):
    name = models.CharField(max_length=120)
    qualifications = models.TextField(null=True)
    expericence = models.TextField(null=True)
    address = models.TextField(null=True)
    time = models.TextField(null=True)
    image_url = models.ImageField(
        upload_to=upload_to_doctors, blank=True, null=True)
    speciality = models.CharField(max_length=100, null=True)
    fee = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name} - {self.mobile}"

    class Meta:
        verbose_name_plural = "Video Call Expert Doctors"
        db_table = "VideoCallExpertDoctor"


class VideoCallExpertDoctorsAppointment(models.Model):
    patient_name = models.CharField(max_length=120)
    patient_age = models.CharField(max_length=120)
    patient_phone = models.CharField(max_length=120)
    details = models.TextField()
    doctor_id = models.ForeignKey(
        VideoCallExpertDoctor, verbose_name="Doctor", on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = "Video Call Expert Doctor Appointment"
        db_table = "VideoCallExpertDoctorsAppointment"
