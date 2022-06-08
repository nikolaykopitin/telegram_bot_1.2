from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu=State()