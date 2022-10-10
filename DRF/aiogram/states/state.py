from aiogram.dispatcher.filters.state import State, StatesGroup

class AddUser(StatesGroup):
    user_id = State()
    photo_id = State()
    full_name = State()


class Authentication(StatesGroup):
    getting_phone_number = State()
    lang = State()

class ToRating(StatesGroup):
    direction = State()

class SelectJob(StatesGroup):
    filter = State()

class MainMenu(StatesGroup):
    to_menu = State()


class Statistic(StatesGroup):
    year = State()
    month = State()
