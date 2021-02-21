from celery import shared_task
from gpiozero import LED

led = LED(21)


@shared_task
def powerOffLed():
    led.off()


@shared_task
def powerOnLed():
    led.on()
