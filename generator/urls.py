from django.conf.urls import include, url
from generator import views
from django.urls import path

app_name = 'generator'

urlpatterns = [
    path('', views.home, name="home"),
    path('Upload_Photo', views.Upload_Photo, name='Upload_Photo'),
    path('home', views.home, name='home'),
    path('create', views.create, name='create'),
    path('show_problem', views.show_problem, name='show_problem'),
    path('show_UserProblem', views.show_UserProblem, name='show_UserProblem'),
    path('OneProblem/<word>/', views.show_OneProblem),
    path('show_UserBlankNum', views.show_UserBlankNum, name='show_UserBlankNum'),
    path('show_DeveloperInfo', views.show_DeveloperInfo, name='show_DeveloperInfo'),
    path("<id>/", views.scan_img_from_DB),
]