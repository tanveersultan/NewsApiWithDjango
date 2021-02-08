from django.urls import path
from newsapp import views


urlpatterns = [
    path('', views.index),
]