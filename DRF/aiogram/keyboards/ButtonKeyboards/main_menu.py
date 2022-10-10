from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu_uz = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="⚙️ Tilni o'zgartirish"),
        KeyboardButton(text="🙋‍♀️🙋‍♂️ Ovoz berish")
        
     ],
     [KeyboardButton(text="🗣 Ovozlarim")]
    ],
    resize_keyboard=True
)

menu_ru = ReplyKeyboardMarkup(
    keyboard=[
     [
        KeyboardButton(text="⚙️ Изменить язык"),
        KeyboardButton(text="🙋‍♀️🙋‍♂️ Голосование")

     ],
     [KeyboardButton(text="🗣 Мои голоса")]

    ],
    resize_keyboard=True
)

menu_en = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="⚙️ Change the language"),
        KeyboardButton(text=" 🙋‍♀️🙋‍♂️ Voting")

     ],
     [
        KeyboardButton(text="🗣 My voices")
     ]
    ],
    resize_keyboard=True
)