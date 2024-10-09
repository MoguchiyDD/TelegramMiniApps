# МогучийДД (MoguchiyDD)
# 2024.09.23, 02:51 PM
# run.py


from asyncio import run, gather
from logging import basicConfig, INFO

from aiogram import Bot, Dispatcher
from app.game import router as gameRouter

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from uvicorn import Config, Server
from threading import Event
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()

_app = FastAPI()
_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stop_event = Event()


async def main() -> None:
    dp.include_router(gameRouter)
    await gather(
        dp.start_polling(bot, skip_updates=True),
        start_fastapi_server()
    )


async def start_fastapi_server():
    config = Config(app=_app, host=getenv("HOST"), port=int(getenv("PORT")))
    server = Server(config)
    await server.serve()


@_app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}


@_app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message: {data}")
            await websocket.send_text(f"Message received: {data}")
    except Exception as e:
        print(f"Connection closed with exception: {e}")
    finally:
        try:
            await websocket.close()
        except Exception as close_exception:
            print(f"Error closing websocket: {close_exception}")


if __name__ == "__main__":
    basicConfig(level=INFO)
    try:
        run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Server and Bot stopped")
