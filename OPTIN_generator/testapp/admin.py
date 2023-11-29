from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Blog)
class adminCountry(admin.ModelAdmin):
    list_display=['title']

# @admin.register(state)
# class adminCountry(admin.ModelAdmin):
#     list_display=['state_name', 'country']

# @admin.register(city)
# class adminCountry(admin.ModelAdmin):
#     list_display=['city_name', "state"]