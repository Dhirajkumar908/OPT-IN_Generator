from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.home, name='home'),
   path('blog', views.blog.as_view(),name='blog'),
   path('blog/<int:pk>', views.detail_blog.as_view(),name='detail_blog'),
   path('blog/create_Blog', views.create_Blog.as_view(), name='create_Blog'),
   path('blog/', views.delete_blog.as_view(), name='delete_blog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)