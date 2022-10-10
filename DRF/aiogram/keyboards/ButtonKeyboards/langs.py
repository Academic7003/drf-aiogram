from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_button = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="🇷🇺 Русский"),
        KeyboardButton(text="🇺🇿 O'zbek")

     ],
     [
        KeyboardButton(text="🇬🇧 English")

     ]
    ],
    resize_keyboard=True
)