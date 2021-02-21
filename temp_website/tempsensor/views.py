from django.shortcuts import render, HttpResponse
from .tasks import powerOnLed, powerOffLed


def enable_led(request):
    powerOnLed.delay()
    return HttpResponse("Power on")


def disable_led(request):
    powerOffLed.delay()
    return HttpResponse("Power on")