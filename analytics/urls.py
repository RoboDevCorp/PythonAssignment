from django.urls import path
from . import views

urlpatterns = [
   path('<str:token>', views.analytics, name='analytics'),
]