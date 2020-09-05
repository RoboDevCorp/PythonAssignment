from django.urls import path
from . import views

urlpatterns = [
    path('', views.generatetoken, name='generatetoken'),
    path('generate', views.generatetoken, name='generatetoken'),
    path('<str:token>', views.navigate, name='navigate'),
]