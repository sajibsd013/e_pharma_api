from django.db import models
from users.models import MyUser

# Create your models here.
class Prescriptions(models.Model):
    prescription = models.TextField()
    user_id = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True )
    class Meta:
        verbose_name_plural = "Prescriptions"
        # db_table = "Prescriptions"

class DoctorInfo(models.Model):
    doctor = models.TextField()
    user_id = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True )
    class Meta:
        verbose_name_plural = "Doctor Info"
        # db_table = "Prescriptions"

class ChiefComplaient(models.Model):
    chief_complaient = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Chief Complaient"
        db_table = "ChiefComplaient"

class History(models.Model):
    history = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "History"
        db_table = "History"

class Examinations(models.Model):
    examinations = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Examinations"
        db_table = "Examinations"

class Diagosis(models.Model):
    diagosis = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Diagosis"
        db_table = "Diagosis"

class Investigations(models.Model):
    investigations = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Investigations"
        db_table = "Investigations"

class Advices(models.Model):
    advices = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Advices"
        db_table = "Advices"

class Followup(models.Model):
    followup = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Followup"
        db_table = "Followup"
