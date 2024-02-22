from django.contrib import admin
from techBlog.models import TechBlog

# Register your models here.
@admin.register(TechBlog)
class TechBlogAdmin(admin.ModelAdmin):
    list_display=['title', 'short_discription', 'content']