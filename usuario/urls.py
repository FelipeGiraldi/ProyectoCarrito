from django.urls import path, include
from .views import *

urlpatterns = [
    path('registrate/', registrate, name="usuario"),
]
