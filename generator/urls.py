from django.conf.urls import include, url
from generator import views
from django.urls import path

urlpatterns = [
    url(r'^upload/$', views.ImageCreateAPIView.as_view()),
    path("<id>/", views.scan_img_from_DB),
]