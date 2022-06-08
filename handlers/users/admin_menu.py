from aiogram import types
from filters import Ls
from loader import dp
from keyboards.default import secret_menu
from data.config import admins


@dp.message_handler(Ls(), text="secret menu", user_id=admins)
async def show_secret_menu(message: types.Message):
    await message.answer("Вы вызвали сектреное меню администратора", reply_markup=secret_menu)
