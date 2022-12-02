from django.urls import path

from . import views
urlpatterns = [
    path('', views.homePage),
    path('get_gear', views.getGear),
]
# add media url to urlpatterns
