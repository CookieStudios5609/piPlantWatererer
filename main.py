from fastapi import FastAPI, WebSocket, staticfiles, WebSocketDisconnect, responses
from sensor import SensorController
import pump
import asyncio



app = FastAPI()
sensor = SensorController()


@app.on_event("startup")
async def start():

    pump.init_gpio()
    app.mount("/", staticfiles.StaticFiles(directory="static", html=True))


@app.websocket("/read_live")
async def live_moisture_data(websocket: WebSocket):
    await websocket.accept()
    try:
        print("Connected to websocket")
        while True:
            await websocket.send_text(str(sensor.read_sensor()))
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        print("Connection to websocket closed")


@app.get("/")
async def redirect_to_main():
    return responses.RedirectResponse(url="/watererer.html")


@app.get("/read_sensor")
async def get_current_moisture():
    return sensor.read_sensor()


@app.on_event("shutdown")
async def close():
    pump.disable_pin()
