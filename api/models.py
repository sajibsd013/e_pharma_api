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
        verbose_name_plural = "Services"
        db_table = "Services"


class Faqs(models.Model):
    ques = models.CharField(max_length=120)
    ans = models.TextField()

    class Meta:
        verbose_name_plural = "FAQs "
        db_table = "Faqs"
