from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from aiogram import types
from states import Talk


@dp.message_handler(text="Поговорить")
async def go_talk(message: types.Message):
    await message.answer("Спросите как у меня дела, либо задайте свой вопрос", reply_markup=ReplyKeyboardRemove())
    await Talk.T1.set()

# @dp.message_handler(state=Talk.T1)
# async def talking_mode(message: types.Message, state: FSMContext):
