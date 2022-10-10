import re
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.db_commands import get_users

menu_cd = CallbackData("show_menu","user_id", "level","rating", "whos_rating", "direction", "lang")

rating_stiker = {'1': '1😣', '2': '2☹️', '3': '3😕', '4': '4😑', '5':'5😍'}

def make_callback_data(level, user_id="0", rating="0", whos_rating="0", direction ="0", lang="0") :
    return menu_cd.new(level=level, user_id=user_id, rating=rating, whos_rating=whos_rating, direction=direction, lang=lang)

async def ortgalar(lang):
    if lang == 'uz':
        text="Ortga",
    elif lang == 'ru':
        text="Назад",
    # if lang == 'en':
    else:
        text="Back",
    return text

async def users_keyboard(direction=False, lang = None, user_list=None):
    users = []
    text = "Назад"
    if lang == 'uz':
        text="Ortga"
    if lang == 'ru':
        text="Назад"
    if lang == 'en':
        text="Back"
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()
    if direction:
        users = await get_users(direction)


        for user in users:
            button_text = f"{user['full_name']}"
            callback_data = make_callback_data(level=CURRENT_LEVEL + 1, user_id=user['user_id'], direction=direction)
            markup.row(
                InlineKeyboardButton(text=button_text, callback_data=callback_data)
            )
        markup.row(
        InlineKeyboardButton(
            text= text,
            callback_data=make_callback_data(level=4, lang=lang)))
    elif user_list:
        for user in user_list:
            button_text = f"{user['full_name']}"
            callback_data = make_callback_data(level=CURRENT_LEVEL + 1, user_id=user['user_id'], direction=direction)
            markup.row(
                InlineKeyboardButton(text=button_text, callback_data=callback_data)
            )
        markup.row(
        InlineKeyboardButton(
            text= text,
            callback_data=make_callback_data(level=4, lang=lang)))
    return markup


async def ratings_keyboard(user_id, direction, lang, user_list=None):
    text = "Назад"
    if lang == 'uz':
        text="Ortga"
    if lang == 'ru':
        text="Назад"
    if lang == 'en':
        text="Back"
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()

    for i in range(1,6):
        button_text = f"{rating_stiker[str(i)]}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           rating=i, user_id=user_id, direction=direction)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    if user_list:
        markup.row(
            InlineKeyboardButton(
                text=text,
                callback_data=make_callback_data(level=4, direction=direction))
        )
    else:
            markup.row(
            InlineKeyboardButton(
                text=text,
                callback_data=make_callback_data(level=4, direction=direction))
        )
    return markup

async def orqaga_keyboard(direction, lang):
    markup = InlineKeyboardMarkup()
    if lang == 'uz':
        text="Ortga"
    if lang == 'ru':
        text="Назад"
    if lang == 'en':
        text="Back"

    markup.row(
        InlineKeyboardButton(
            text=text,
            callback_data=make_callback_data(level=4, direction=direction))
    )
    return markup

async def cancel_rating_keyboard(user_id, whos_rating, direction, lang):
    if lang == 'uz':
        text="Ortga"
        text1 ="Bekor qilish"
    if lang == 'ru':
        text="Назад"
        text1 ="Отмена"
    if lang == 'en':
        text="Back"
        text1 ="Cancel"

    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text=text,
            callback_data=make_callback_data(level=4, direction=direction))
    )
    markup.row(
        InlineKeyboardButton(
            text=text1,
            callback_data=make_callback_data(level=3, whos_rating=whos_rating, user_id=user_id, direction=direction ))
    )
    return markup