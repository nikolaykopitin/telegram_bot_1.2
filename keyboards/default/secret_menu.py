from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

secret_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Секретная информация")
        ],
        [
            KeyboardButton(text="Убрать клавиатуру"),
        ],
    ],
    resize_keyboard=True
)
