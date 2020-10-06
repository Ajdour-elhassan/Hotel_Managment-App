from django.urls import path
from . import views

urlpatterns = [
   path('', views.home , name="home"),
   path('about_page' , views.about , name='about'),
   path('dashbord' , views.dashbord , name='dashbord')
]
