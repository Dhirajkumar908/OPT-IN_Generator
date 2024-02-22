from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.userlogin, name='userlogin'), 
    path('user_logout', views.user_logout, name='user_logout'),   
    path('optin',views.Add_OPTIN, name='Add_OPTIN'),   
    path('delete/<int:id>', views.delete_optin, name='delete_optin'),  
    path('headerfooter', views.headerfooter, name='headerfooter'),
    path('upload_csv', views.upload_csv, name="upload_csv"),
    path('dlt_all', views.dlt_all, name='dlt_all')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)