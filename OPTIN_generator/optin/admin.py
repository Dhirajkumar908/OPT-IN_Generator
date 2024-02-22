from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(OptIN)
class AdminOptin(admin.ModelAdmin):
    list_display=['name', 'number', 'email', 'data']

@admin.register(HeaderFooter)
class AdminHeaderFooter(admin.ModelAdmin):
    list_display=['name', 'header', 'footer']




#// change the site name

admin.site.site_header = "DKoptin"

# #//change the site title

admin.site.site_title = "DKoptin"

#admin site intex title
admin.site.index_title = 'OPT-IN Genarator Admin Dashbord'   