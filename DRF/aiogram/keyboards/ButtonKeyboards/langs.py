from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_button = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="๐ท๐บ ะ ัััะบะธะน"),
        KeyboardButton(text="๐บ๐ฟ O'zbek")

     ],
     [
        KeyboardButton(text="๐ฌ๐ง English")

     ]
    ],
    resize_keyboard=True
)