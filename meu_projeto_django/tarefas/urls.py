from django.urls import path
from .views import ola_django

urlpatterns = [
    path('', ola_django)
]