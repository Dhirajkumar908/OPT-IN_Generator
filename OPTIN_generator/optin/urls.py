from django.urls import path

from . import views
from .views import optinListView, delete_Optin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',optinListView.as_view(), name='optinListView' ),
    path('delete/<int:id>/', views.delete_Optin.as_view(), name='delete_Optin'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)