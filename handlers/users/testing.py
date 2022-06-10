from aiogram.dispatcher.storage import FSMContext

from keyboards.default import menu
from loader import dp
from aiogram import types
from states import Test


@dp.message_handler(state=Test.Q1)
async def answer_on_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("Ваш возраст")
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_on_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("спасибо за ваши ответы", reply_markup=menu)
    await message.answer(f"Ответ на вопрос 1: {answer1}")
    await message.answer(f"Ответ на вопрос 2: {answer2}")
    await state.reset_state()
