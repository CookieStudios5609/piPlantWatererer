import Adafruit_ADS1x15 as ads


class SensorController:
    def __init__(self, new_gain: int = 1, index: int = 0):
        """A class to control a capacitive soil moisture sensor, connected to an ADS1115, connected to the Pi with
        the default pins used in the library, or at the link here:
        https://github.com/WayinTop/Automatic-Plant-Watering-System-Tutorial/blob/master/Raspberry%20Pi%20Plant%20Watering%20System/1%20channel%20Plant%20Watering%20System%20with%20Raspberry%20Pi.pdf

         Index refers to one of the 4 available channels to read from. Which you use will depend on
         which you're using from "A0" to "A3." """
        self.adc = ads.ADS1115()
        self.gain = new_gain
        self.channel = index

    def read_sensor(self):
        return int(self.adc.read_adc(self.channel, gain=self.gain))


