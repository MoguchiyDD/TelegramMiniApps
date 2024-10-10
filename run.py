# МогучийДД (MoguchiyDD)
# 2024.09.23, 02:51 PM
# run.py


from asyncio import run, gather
from logging import basicConfig, INFO

from aiogram import Bot, Dispatcher
from app.game import router as gameRouter

from dotenv import load_dotenv
from os import getenv

load_dotenv()

bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


async def main() -> None:
    dp.include_router(gameRouter)
    dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    basicConfig(level=INFO)
    try:
        run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
