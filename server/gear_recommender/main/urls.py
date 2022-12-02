from django.urls import path

from . import views
urlpatterns = [
    path('', views.homePage)
]
# add media url to urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)