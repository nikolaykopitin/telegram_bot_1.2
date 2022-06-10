from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Спросить")
        ],
        [
            KeyboardButton(text="Информация")
        ],
        [
            KeyboardButton(text="Заполнить анкету")
        ],
        [
            KeyboardButton(text="Убрать клавиатуру"),
        ],
    ],
    resize_keyboard=True
)
