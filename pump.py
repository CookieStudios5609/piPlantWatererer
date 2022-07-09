import RPi.GPIO as GPIO
import time

# developing for pi-specific libraries without a remote dev plugin is pain. Shame vscode's remote crashes the thing
# TODO: Go back to the idea of implementing a PumpController class. Support multiple pumps and sensors.


def init_gpio(pin: int = 21):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)


def pump_timed(seconds: int = 3):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(21, GPIO.LOW)


def pump_on(pin: int = 21):
    GPIO.output(pin, GPIO.HIGH)


def pump_off(pin: int = 21):
    GPIO.output(pin, GPIO.LOW)


def disable_pin(pin: int = 21):
    GPIO.cleanup(pin)
