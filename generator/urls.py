from django.conf.urls import include, url
from generator import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('Upload_Photo', views.Upload_Photo),
    path('create', views.create, name='create'),
    url(r'^upload/$', views.ImageCreateAPIView.as_view()),
    path("<id>/", views.scan_img_from_DB),
]