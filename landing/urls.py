from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'landing'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('gallery/upload_photo',
         views.UploadPhotoView.as_view(),
         name='upload_photo'),
    path('gallery/<int:pk>/', views.delete_photo, name='delete_photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns.append(
        path('gallery/', views.PhotoListView.as_view(), name='gallery'))
