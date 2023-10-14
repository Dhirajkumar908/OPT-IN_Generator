from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.Add_OPTIN, name='Add_OPTIN'),   
    path('delete/<int:id>',views.delete_optin, name='delete_optin' ),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)