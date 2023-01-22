from email.policy import default
from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=120)
    depertment = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    salary = models.CharField(max_length=120)
    last_date = models.DateTimeField(blank=True, null=True)
    working_schedule = models.CharField(max_length=120)
    job_nature = models.CharField(max_length=120)
    requirements = models.TextField()
    responsibilities = models.TextField()
    benefits  = models.TextField()

    class Meta:
        verbose_name_plural = "Job"
        db_table = "Job"

