> Use this at your own risk. The creator of this repo is not responsible to any damage that may come from the use of this program or wiring guides used when setting up this program. 
# piPlantWatererer: An API for monitoring soil moisture and watering plants accordingly

I've had a Raspberry Pi 3a+ sitting around for a bit only being used as another node in my homelab. Time to do something more than running an LED with its GPIO pins.
# Project Structure:

/: The root folder contains `run.py`, the file to run to start the entire program, and `main.py`, the file that holds most of the FastAPI logic. `pump.py` and `sensor.py` contain functions that control a relay and ADS1115 module respectively. 

/static: This folder holds the static files exposed to port 8000 by FastAPI. Right now, these consist of a simple html layout, `watererer.js`, which connects to a FastAPI websocket and updates text on the site, and some cheesy styling.

# Setup

To use:
1. Connect your pi to your relay, sensor, and ADC accordingly. Use BCM pin 21 for the relay control.
2. On your Pi, run `git clone https://github.com/CookieStudios5609/piPlantWatererer.git'
3.  `cd piPlantWatererer`
4. `python -m pip install -r requirements.txt`
5. `python run.py` 


The webpage should now be visible at 0.0.0.0:8000 if accessed on the Raspberry Pi itself, and should redirect to /watererer.html automatically.

# Usage

Most features are not implemented. To view, visit http://<your Pi's local ipv4>:8000/watererer.html in a web browser if 

# Future

<ul>
  <li> [ ] Implement buttons and an integer form to manually enable/disable pump </li>
  <li> [ ] Implement storage for scheduled watering</li>
  <li> [ ] Implement status page with details on the last watering, uptime, and next watering</li>
  <li> [ ] Allow user-set thresholds for moisture (TOO DRY, DRY, AVERAGE, WET) and allow watering based on these</li>
  <li> [ ] Implement FIDO2 auth and a settings page for the above</li>
</ul>



