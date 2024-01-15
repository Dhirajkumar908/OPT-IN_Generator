from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(OptIN)
class AdminOptin(admin.ModelAdmin):
    list_display=['name', 'number', 'email', 'data']

@admin.register(HeaderFooter)
class AdminHeaderFooter(admin.ModelAdmin):
    list_display=['name', 'header', 'footer']



