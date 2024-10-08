# МогучийДД (MoguchiyDD)
# 2024.09.23, 05:10 PM
# game.py


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


def gameBoard():
    """
    """

    board = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Minesweeper",
                    web_app=WebAppInfo(url="https://moguchiydd.github.io/TelegramMiniMinesweeper/")
                )
            ]
        ],
        resize_keyboard=True
    )
    return board
