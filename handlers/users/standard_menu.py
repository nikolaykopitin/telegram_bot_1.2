from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types

from states import Test
from utils.misc import rate_limit


@dp.message_handler(Command('keyboard'))
async def show_menu(message: types.Message):
    await message.answer('клавиатура', reply_markup=menu)


@rate_limit(5, 'help')
@dp.message_handler(text="Информация")
async def get_info(message: types.Message):
    await message.answer("Здесь какая-то информация")


@dp.message_handler(text="Убрать клавиатуру")
async def close_keyboards(message: types.Message):
    await message.answer("Выход", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Заполнить анкету")
async def go_test(message: types.Message):
    await message.answer("Как вас зовут?", reply_markup=ReplyKeyboardRemove())
    await Test.Q1.set()