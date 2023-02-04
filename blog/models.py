from django.db import models
from django.utils.timezone import now
from users.models import MyUser


# Create your models here.

def upload_to_blog(instance, filename):
    return 'images/blog/{filename}'.format(filename=filename)


class Blog(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120, null=True , blank=True)
    keywords = models.CharField(max_length=120 , null=True , blank=True)
    image_url = models.ImageField(
        upload_to=upload_to_blog, null=True , blank=True)
    user = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, null=True, blank=True, related_name='blog')
    short_desc = models.TextField(null=True , blank=True)
    desc  = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Blog Post"
        db_table = "Blog"



class Comment(models.Model):
    comment = models.CharField(max_length=120)
    user = models.ForeignKey(
        MyUser, verbose_name="User", on_delete=models.CASCADE, related_name='comment')
    blog = models.ForeignKey(
        Blog, verbose_name="Blog", on_delete=models.CASCADE, related_name='comment')
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = "Blog Comment"
        db_table = "Comment"

