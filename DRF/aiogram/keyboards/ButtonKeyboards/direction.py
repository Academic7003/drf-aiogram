from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


direction_button_uz = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="🛎 Qabulxona"),
        KeyboardButton(text="💸 Kassa")

     ],
     [
        KeyboardButton(text="🩺 Shifokor")

     ],
     [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)
direction_button_ru = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="🛎 Прием"),
        KeyboardButton(text="💸 Касса")

     ],
     [
        KeyboardButton(text="🩺 Доктор")
     ],
     [KeyboardButton(text="⬅️ Назад")]


    ],
    resize_keyboard=True
)


direction_button_en = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="🛎 Reception"),
        KeyboardButton(text="💸 Box office")

     ],
     [
        KeyboardButton(text="🩺 Doctor")
     ],
     [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)