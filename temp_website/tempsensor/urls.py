from django.urls import path

from . import views

urlpatterns = [
    path('enable_led', views.enable_led, name='enable_led'),
    path('disable_led', views.diable_led, name='disable_led'),
]