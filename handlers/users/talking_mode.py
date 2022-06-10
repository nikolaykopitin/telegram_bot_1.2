from aiogram.dispatcher import FSMContext

from keyboards.default import menu
from loader import dp
from aiogram import types
from states import Talk

import random
import nltk
# import json


@dp.message_handler(state=Talk.T1)
async def get_message(message: types.Message, state: FSMContext):
    user_intents = {
        'intents': {
            'hello': {
                'examples': ['Привет!', 'хэллоу', 'добрый день!!'],
                'responses': ['хай', 'Здравствуйте', 'Доброе утро!']
            },
            'bye': {
                'examples': ['Пока!', 'увидимся', 'счастливо', 'выход'],
                'responses': ['до свиданья', 'до скорых встреч', 'Спокойной ночи)']
            },
            "mood": {
                "examples": [
                    "что делаешь",
                    "как настроение",
                    "грустишь?",
                    "как дела",
                    "как сам",
                    "как дела?",
                    "как настроение?"
                ],
                "responses": [
                    "бывало лучше",
                    "нормально",
                    "отлично!",
                    "да так",
                    "спасибо, что интересуетесь! Хорошо"
                ]
            }
        }
    }

    chat_id = message.chat.id
    input_text = str(message.text)
    print(input_text)

    def clean(text):
        clean_text = ''

        for char in text.lower():
            if char in 'абвгдеёжзийклмнопрстуфхцчшщьыьэюяabcdefghijklmnoqrstuvwxyz':
                clean_text = clean_text + char
        return clean_text

    def get_intent(text):
        for intent in user_intents['intents'].keys():
            for example in user_intents['intents'][intent]['examples']:
                s1 = clean(example)
                s2 = clean(text)
                if nltk.edit_distance(s1, s2) / max(len(s1), len(s2)) < 0.4:
                    return intent
        return 'intent not found :('

    def choice(text):
        intent = get_intent(text)
        if intent != 'intent not found :(':
            return random.choice(user_intents['intents'][intent]['responses'])
        else:
            return 'я не понял, попробуйте сформулировать по-другому'
    answer = choice(input_text)
    new_intent = get_intent(input_text)
    bot = dp.bot
    print(new_intent)
    if new_intent == 'bye':
        await state.reset_state()
        await bot.send_message(chat_id=chat_id, text="Вы вышли из разговорного режима", reply_markup=menu)

    await bot.send_message(chat_id=chat_id, text=answer)

