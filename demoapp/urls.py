from django.urls import path
from . import views

urlpatterns  = [
    path('', views.home, name='home'),
    # path('home', views.home, name='home'),
    path('format', views.format_view, name='format'),
] 