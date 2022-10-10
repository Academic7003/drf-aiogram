from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.db_api.db_commands import get_jobs


async def jobs_maker(direction):
    keyboard = []
    chunk = []
    for i in await get_jobs(direction):
        if len(chunk)<2:
            chunk.append(KeyboardButton(text=i['name']))
        if len(chunk)==2:
            keyboard.append(chunk)
            chunk = []
    return keyboard


async def jobs_button_maker(direction):
    
    jobs_button = ReplyKeyboardMarkup(keyboard=await jobs_maker(direction), resize_keyboard=True)
    return jobs_button




