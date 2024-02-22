from django.urls import path
from techBlog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.posts_list_views.as_view(), name='posts_list_views'),
    path('detail_view/<int:pk>', views.detail_view, name='detail_view'),
    path('create_post', views.create_post, name='create_post')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)