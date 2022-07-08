import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15 as ads

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

GAIN=1
adc = ads.ADS1115()
values = adc.read_adc(0,gain=GAIN)
print(values)
time.sleep(1)
values = adc.read_adc(0,gain=GAIN)
print(values)

print("on")
GPIO.output(21,GPIO.HIGH)
time.sleep(2)
print("on not")
GPIO.output(21,GPIO.LOW)
GPIO.cleanup(21)
#using board pins 4, 6, and 40 for this. 4 gets the vcc from the relay, 6 gets the gnd from the relay, 40 (21) gets the IN pin
#others using wayintop github guide
