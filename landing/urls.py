from django.urls import path

from landing import views

urlpatterns = [
    url(r'^', views.landing, name='landing'),
]