from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from utils.db_api.db_commands import *
stat_cd = CallbackData("statistic", 'level', 'user_job', 'user_id', 'month', 'year', 'direction',)

mnths={
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}


def make_statistic_data(level, user_job="0", user_id="0", month="0", year="0", direction="0"):
    return stat_cd.new(direction=direction, user_job=user_job, user_id=user_id, month=month, year=year, level=level)
async def choose_direction():

    markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kassa")
        ],
        [
            KeyboardButton(text="Shifokor"),
            KeyboardButton(text="Qabulxona")
        ],
    ],
    resize_keyboard=True
)
    return markup


async def choose_job(direction):
    jobs = await get_jobs(direction)
    keyboard = []
    chunk = []
    for i in jobs:
        if len(chunk) < 2:
            chunk.append(KeyboardButton(text=f"{i['name']}"))
        else:
            keyboard.append(chunk)
            chunk = []
            chunk.append(KeyboardButton(text=f"{i['name']}"))
    if len(chunk) == 1:
        keyboard.append(chunk)
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    return markup


async def choose_user(user_job):
    users = await get_user_sort_job(user_job)
    keyboard = []
    chunk = []
    for i in users:
        if len(chunk) < 2:
            chunk.append(KeyboardButton(text=f"{i['full_name']}"))
        else:
            keyboard.append(chunk)
            chunk = []
            chunk.append(KeyboardButton(text=f"{i['full_name']}"))
    if len(chunk) == 1:
        keyboard.append(chunk)
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    return markup


async def choose_year(full_name):
    keyboard = []
    chunk = []
    years = []
    user_ratings = await get_user_given_raitings(full_name)
    for i in user_ratings:
        year = i['date'].split('-')[0]
        if not year in years:
            years.append(year)

    for i in years:
        if len(chunk) < 2:
            chunk.append(KeyboardButton(text=f"{i}"))
        else:
            keyboard.append(chunk)
            chunk = []
            chunk.append(KeyboardButton(text=f"{i}"))
    if len(chunk) == 1:
        keyboard.append(chunk)
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return markup


async def choose_month(full_name):
    keyboard = []
    chunk = []
    months = []
    user_ratings = await get_user_given_raitings(full_name)
    for i in user_ratings:
        month = i['date'].split('-')[1]
        if month not in months:
            months.append(month)

    for i in months:
        if len(chunk) < 2:
            chunk.append(KeyboardButton(text=f"{mnths[int(i)]}"))
        else:
            keyboard.append(chunk)
            chunk = []
            chunk.append(KeyboardButton(text=f"{mnths[int(i)]}"))
    if len(chunk) == 1:
        keyboard.append(chunk)
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return markup
