from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.athlete_profile, name='profile'),
    path('sample1/', views.sample1, name='sample1'),
]