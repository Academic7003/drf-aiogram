from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.db_api.db_commands import *
from loader import _



contact_button_uz = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="📞 Mening raqamim", request_contact=True)
     ]

    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

contact_button_ru = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="📞 Мой номер", request_contact=True)
     ]

    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

contact_button_en = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="📞 My number", request_contact=True)
     ]

    ],
    one_time_keyboard=True,
    resize_keyboard=True
)