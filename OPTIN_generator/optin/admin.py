from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(OptIN)
class AdminOptin(admin.ModelAdmin):
    list_display=['name', 'number', 'email', 'data']

@admin.register(HeaderFooter)
class AdminHeaderFooter(admin.ModelAdmin):
    list_display=['Name', 'header', 'footer']


# @admin.register(company)
# class admincompany(admin.ModelAdmin):
#     list_display=['company_name','company_header','company_footer']
