from django.contrib import admin
from .models import Blog, Comment


# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "category","created_date"]

    class Meta:
        model = Blog


admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment"]

    class Meta:
        model = Comment


admin.site.register(Comment, CommentAdmin)

