# МогучийДД (MoguchiyDD)
# 2024.09.23, 03:00 PM
# start.py


from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.game import gameBoard

router = Router()


@router.message(Command("game"))
async def cmdStart(message: Message):
    """
    """
    
    await message.answer("Выберите игру:", reply_markup=gameBoard())
