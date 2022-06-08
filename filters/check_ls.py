from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class Ls(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE
