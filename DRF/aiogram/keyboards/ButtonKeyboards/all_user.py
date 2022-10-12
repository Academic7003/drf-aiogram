from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from utils.db_api.db_commands import *
stat_cd = CallbackData("statistic", 'level', 'user_job', 'user_id', 'month', 'year', 'direction')

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
    return stat_cd.new( direction=direction, user_job=user_job, user_id=user_id, month=month, year=year, level=level)


async def choose_direction():
    CURRENT_LEVEL = 0

    markup = InlineKeyboardMarkup()
    for i in ["Kassa", 'Shifokor', 'Qabulxona']:
        callback_data = make_statistic_data(level=CURRENT_LEVEL + 1, direction=i)
        markup.row(
            InlineKeyboardButton(text=i, callback_data=callback_data)
        )
    return markup


async def choose_job(direction):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    jobs = await get_jobs(direction)
    print("w"*100, jobs, direction)
    for i in jobs:
        callback_data = make_statistic_data(level=CURRENT_LEVEL + 1, user_job=i['name'])
        markup.row(
            InlineKeyboardButton(text=i['name'], callback_data=callback_data)
        )
    return markup


async def choose_user(user_job):
    CURRENT_LEVEL = 2
    users = await get_user_sort_job(user_job)
    markup = InlineKeyboardMarkup()

    for i in users:
        callback_data = make_statistic_data(level=CURRENT_LEVEL + 1, user_job=user_job, user_id=i['user_id'])
        markup.row(
            InlineKeyboardButton(text=i['full_name'], callback_data=callback_data)
        )
    return markup


async def choose_year(user_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()

    years = []
    user_ratings = await get_user_given_raitings(user_id)
    for i in user_ratings:
        year = i['date'].split('-')[0]
        if not year in years:
            years.append(year)

    for i in years:
        callback_data = make_statistic_data(level=CURRENT_LEVEL + 1, user_id=user_id, year=i )
        markup.row(
            InlineKeyboardButton(text=i, callback_data=callback_data)
        )
    return markup


async def choose_month(user_id, year):
    CURRENT_LEVEL = 4
    markup = InlineKeyboardMarkup()

    months = []
    user_ratings = await get_user_given_raitings(user_id)
    for i in user_ratings:
        month = i['date'].split('-')[1]
        if month not in months:
            months.append(month)

    for i in months:
        callback_data = make_statistic_data(level=CURRENT_LEVEL+1, user_id=user_id, year=year, month=int(i))
        markup.row(
            InlineKeyboardButton(text=mnths[int(i)], callback_data=callback_data)
        )
    return markup
