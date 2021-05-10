from django.conf.urls import include, url
from generator import views
from django.urls import path

app_name = 'generator'

urlpatterns = [
    path('', views.home, name="home"),
    path('Upload_Photo', views.Upload_Photo, name='Upload_Photo'),
    path('create', views.create, name='create'),
    path('show_problem', views.show_problem, name='show_problem'),
    url(r'^upload/$', views.ImageCreateAPIView.as_view()),
    path("<id>/", views.scan_img_from_DB),
]