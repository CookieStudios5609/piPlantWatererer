from fastapi import FastAPI, status, Response
from sensor import SensorController
import pump


app = FastAPI()


@app.on_event("startup")
async def start():
    sensor = SensorController()
    pump.init_gpio()


@app.get("/")
async def root():
    return status.HTTP_200_OK

