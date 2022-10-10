from ast import Await
from datetime import datetime
from email import message
from typing import Union
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery, Message
from keyboards.inline.menu_keyboards import menu_cd, users_keyboard, ratings_keyboard, orqaga_keyboard, cancel_rating_keyboard
from loader import dp, _ , bot 
from utils.db_api.db_commands import *
from data import config
from states.state import AddUser, Authentication, ToRating, SelectJob, MainMenu, Statistic
from aiogram.dispatcher import FSMContext
from keyboards.ButtonKeyboards.langs import language_button
from keyboards.ButtonKeyboards.contact import *
from keyboards.ButtonKeyboards.direction import *
from keyboards.ButtonKeyboards.jobs import jobs_button_maker
from keyboards.ButtonKeyboards.main_menu import *

import os
import requests

admin_id = config.admins
dic = {}
chat_id = 0
markup = ''
async def jobs_soort():
    jobs = get_jobs('Shifokor')
    jobs_list = [i['name'] for i in jobs]
    return jobs_list

@dp.message_handler(Command("start"), state="*")
async def auth_or_rating(message : types.Message, state: FSMContext):
    global chat_id
    await state.finish()
    user_id = message.from_user.id
    chat_id = message.chat.id
    user = await get_ratinger(user_id=user_id)
    if user:
        try:
            user_lang =await get_user_lang(user_id)
            if user_lang == 'uz':
                await message.answer(("📲 Asosiy menu"), reply_markup=menu_uz)
            elif user_lang == 'ru':
                await message.answer(("📲 Главное меню"), reply_markup=menu_ru)
            else:
                await message.answer(("📲 Main menu"), reply_markup=menu_en)
            await MainMenu.to_menu.set()
        except:
            # await add_ratinger(user_id=user_id)
            await message.answer("Assalomu alaykum! xush kelibsiz.\n\nЗдравствуйте! Добро пожаловать.\n\nHello! Welcome.", reply_markup=language_button)
            await Authentication.lang.set()
    else:
        await add_ratinger(user_id=user_id)
        await message.answer("Assalomu alaykum! xush kelibsiz.\n\nЗдравствуйте! Добро пожаловать.\n\nHello! Welcome.", reply_markup=language_button)
        await Authentication.lang.set()

@dp.message_handler(Text(equals=["⚙️ Tilni o'zgartirish","🙋‍♀️🙋‍♂️ Ovoz berish","🗣 Ovozlarim","⚙️ Change the language", "🙋‍♀️🙋‍♂️ Voting","🗣 My voices","🙋‍♀️🙋‍♂️ Голосование","⚙️ Изменить язык","🗣 Мои голоса"]), state=MainMenu.to_menu)
async def main_menu(message: Message):
    user_id = message.from_user.id
    user_lang = await get_user_lang(user_id)
    text = message.text
    a = await get_ratinger_raitings(message.from_user.id)

    if text in ["⚙️ Tilni o'zgartirish", "⚙️ Change the language","⚙️ Изменить язык"]:
        await message.answer(text, reply_markup=language_button)
        await Authentication.lang.set()
    elif text == "🙋‍♀️🙋‍♂️ Ovoz berish":
        await message.answer(("Qanday xizmat ko'rsatishga fikr qoldirasiz?"), reply_markup=direction_button_uz)
        await ToRating.direction.set()
    elif text == "🙋‍♀️🙋‍♂️ Voting":
        await message.answer(("What kind of service would you like to offer?"), reply_markup=direction_button_en)
        await ToRating.direction.set()
    elif text == "🙋‍♀️🙋‍♂️ Голосование":
        await message.answer(("На какую обслуживание хотите оставить отзыв"), reply_markup=direction_button_ru)
        await ToRating.direction.set()
    elif text == "🗣 Ovozlarim":
        txt = "Sizning ovozlaringiz\n"
        for k,i in enumerate(a):
            job = await get_user_raitinger_direction(int(i['whos_rating']))
            name = await get_user(int(i['whos_rating']))
            txt +=f'{k+1}){job} - {name["full_name"]} - {i["rating"]}\n'
        await message.answer(txt)
        if user_lang == 'uz':
            await message.answer(("📲 Asosiy menu"), reply_markup=menu_uz)
        elif user_lang == 'ru':
            await message.answer(("📲 Главное меню"), reply_markup=menu_ru)
        else:
            await message.answer(("📲 Main menu"), reply_markup=menu_en)
        await MainMenu.to_menu.set()
    elif text == "🗣 My voices":
        txt = "Your voices\n"
        for k,i in enumerate(a):
            job = await get_user_raitinger_direction(int(i['whos_rating']))
            name = await get_user(int(i['whos_rating']))

            txt +=f'{k+1}){job} - {name["full_name"]} - {i["rating"]}\n'
        await message.answer(txt)
        if user_lang == 'uz':
            await message.answer(("📲 Asosiy menu"), reply_markup=menu_uz)
        elif user_lang == 'ru':
            await message.answer(("📲 Главное меню"), reply_markup=menu_ru)
        else:
            await message.answer(("📲 Main menu"), reply_markup=menu_en)
        await MainMenu.to_menu.set()
    elif text == "🗣 Мои голоса" :
        txt = "Ваши голоса\n"
        for k,i in enumerate(a):
            print(i, "_-"*100)
            job = await get_user_raitinger_direction(int(i['whos_rating']))
            name = await get_user(int(i['whos_rating']))
            txt +=f'{k+1}){job} - {name["full_name"]} - {i["rating"]}\n'
        await message.answer(txt)
        if user_lang == 'uz':
            await message.answer(("📲 Asosiy menu"), reply_markup=menu_uz)
        elif user_lang == 'ru':
            await message.answer(("📲 Главное меню"), reply_markup=menu_ru)
        else:
            await message.answer(("📲 Main menu"), reply_markup=menu_en)
        await MainMenu.to_menu.set()
    
    
@dp.message_handler(Text(equals=["🇷🇺 Русский", "🇺🇿 O'zbek", "🇬🇧 English"]), state=Authentication.lang)
async def set_language(message: Message):
    user_id = message.from_user.id
    user = await get_ratinger(user_id)
    print(message.text)
    if message.text == "🇷🇺 Русский":
        await add_lang_to_user(user_id,'ru')
    elif message.text == "🇺🇿 O'zbek":
        await add_lang_to_user(user_id,'uz')
    elif message.text == "🇬🇧 English":
        await add_lang_to_user(user_id,'en')
    user_lang = await get_user_lang(user_id)
    
    if user['phone_number']:
        if user_lang == 'uz':
            await message.answer(("📲 Asosiy menu"), reply_markup=menu_uz)
        elif user_lang == 'ru':
            await message.answer(("📲 Главное меню"), reply_markup=menu_ru)
        else:
            await message.answer(("📲 Main menu"), reply_markup=menu_en)
        await MainMenu.to_menu.set()
    else:
        if user_lang == 'uz':
            await message.answer("Telefon raqamingizni kiriting:", reply_markup=contact_button_uz)

        elif user_lang == 'ru':
            await message.answer("Введите свой номер телефона:", reply_markup=contact_button_ru)

        elif user_lang == 'en':
            await message.answer("Enter your phone number:", reply_markup=contact_button_en)

        await Authentication.getting_phone_number.set()


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=Authentication.getting_phone_number)
async def get_phone_number(message: Message, state:FSMContext):
    user_id = message.from_user.id
    user_lang = await get_user_lang(user_id)
    mobile = message.contact.phone_number.replace('+', '')
    await add_phone_to_user(phone_number=f'{mobile}', user_id=user_id)
    if user_lang == 'uz':
            await message.answer(("Qanday xizmat ko'rsatishga fikr qoldirasiz?"), reply_markup=direction_button_uz)
            await ToRating.direction.set()
    elif user_lang == 'ru':
            await message.answer(("На какую обслуживание хотите оставить отзыв"), reply_markup=direction_button_ru)
            await ToRating.direction.set()
    if user_lang == 'en':
            await message.answer(("What kind of service would you like to offer?"), reply_markup=direction_button_en)
            await ToRating.direction.set()


@dp.message_handler(Text(equals=["🩺 Shifokor", "💸 Kassa", "🛎 Qabulxona", "🛎 Прием", "💸 Касса", "🩺 Доктор", "🩺 Doctor", "💸 Box office", "🛎 Reception", "⬅️ Orqaga", "⬅️ Назад", "⬅️ Back" ]), state=ToRating.direction)
async def get_direction(message: Message, state:FSMContext):
    markup = ''
    user_id = message.from_user.id
    user_lang = await get_user_lang(user_id)
    if message.text in ["🩺 Shifokor", "🩺 Доктор", "🩺 Doctor"]:
        
        markup = await jobs_button_maker("Shifokor")
        await message.answer("{message_text}:".format(message_text=message.text), reply_markup=markup)
        await SelectJob.filter.set()
    else:
        if message.text in ["💸 Kassa", "💸 Касса", "💸 Box office" ]:
            markup = await users_keyboard("Kassa", user_lang)
        elif message.text in ["🛎 Qabulxona", "🛎 Прием", "🛎 Reception"]:
            markup = await users_keyboard("Qabulxona", user_lang)

        elif message.text in ["⬅️ Orqaga", "⬅️ Назад", "⬅️ Back"]:
            if user_lang == 'uz':
                await message.answer(("📲 Asosiy menu"), reply_markup=menu_uz)
            elif user_lang == 'ru':
                await message.answer(("📲 Главное меню"), reply_markup=menu_ru)
            else:
                await message.answer(("📲 Main menu"), reply_markup=menu_en)
            return await MainMenu.to_menu.set()

        await message.answer("{message_text}:".format(message_text=message.text), reply_markup=markup)
        await message.delete()
        await state.finish()
    A =  message.message_id
    B = message.chat.id
    await bot.delete_message(chat_id = B, message_id=A-1)


    


@dp.message_handler( state=SelectJob.filter)
async def sort_user_job(message: Message, state: FSMContext):
    user_id = message.from_user.id
    A =  message.message_id
    print(message.text)
    B = message.chat.id
    print(str(A), "-"*10)
    await bot.delete_message(chat_id = B, message_id=A-1)
    await bot.delete_message(chat_id = B, message_id=A-2)


    user_lang = await get_user_lang(user_id)
    list = await get_user_sort_job(message.text)
    print(user_lang*100)
    markup = await users_keyboard(lang=user_lang,  user_list = list )
    await message.delete()

    await message.answer(text=message.text, reply_markup=markup)
    await state.finish()

async def users_choice(message: Union[CallbackQuery, Message], direction, **kwargs):
    user_id = message.from_user.id
    user_lang = await get_user_lang(user_id)
    if isinstance(message, Message):
        if user_lang == 'uz':
            await message.answer("Reyting qoldirish uchun tanlang", reply_markup=await users_keyboard(direction,user_lang))
        if user_lang == 'ru':
            await message.answer("Выберите, чтобы оставить оценку", reply_markup=await users_keyboard(direction,user_lang))
        if user_lang == 'en':
            await message.answer("Choose to leave a raiting", reply_markup=await users_keyboard(direction,user_lang))
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.delete()
        if user_lang == 'uz':
            await call.message.answer("Reyting qoldirish uchun tanlang", reply_markup=await users_keyboard(direction,user_lang))
        if user_lang == 'ru':
            await call.message.answer("Выберите, чтобы оставить оценку", reply_markup=await users_keyboard(direction,user_lang))
        if user_lang == 'en':
            await call.message.answer("Choose to leave a rating", reply_markup=await users_keyboard(direction,user_lang))
        await call.message.delete()


async def list_rayting(callback: CallbackQuery, user_id, direction, **kwargs):
    user_id1 = callback.from_user.id
    user_lang = await get_user_lang(user_id1)
    markup = await ratings_keyboard(user_id, direction, user_lang)
    a = await get_user(int(user_id))
    full= a['full_name']
    img_id = a['photo_id']
    await callback.message.delete()
    if user_lang == 'uz':
        await callback.message.answer_photo(photo=img_id, caption='{full}ga raiting:'.format(full=full), reply_markup=markup)
    if user_lang == 'ru':
        await callback.message.answer_photo(photo=img_id, caption='Рейтинг {full}:'.format(full=full), reply_markup=markup)
    if user_lang == 'en':
        await callback.message.answer_photo(photo=img_id, caption='Rating to {full}'.format(full=full), reply_markup=markup)


async def add_user_rating(callback: CallbackQuery, user_id, rating, level, direction, **kwargs):
    a = False
    b = False
    user_id1 = callback.from_user.id
    user_lang = await get_user_lang(user_id1)
    if int(callback.from_user.id) != int(user_id):
        slovar = await get_user_given_raitings(user_id)
        for i in slovar:
            if int(i['whos_rating']) == int(user_id) and int(i['ratinger']) == int(callback.from_user.id):
                a = True
                break
        if a:
            await callback.message.delete()
            if user_lang == 'uz':
                await callback.message.answer("Ushbu Userga raiting qo'ygansiz!", reply_markup=await cancel_rating_keyboard(callback.from_user.id, user_id, direction,user_lang))
            if user_lang == 'ru':
                await callback.message.answer("Вы оценили этого пользователя!", reply_markup=await cancel_rating_keyboard(callback.from_user.id, user_id, direction,user_lang))
            if user_lang == 'en':
                await callback.message.answer("You rated this user!", reply_markup=await cancel_rating_keyboard(callback.from_user.id, user_id, direction,user_lang))

        else:
            await add_rating(ratinger=int(callback.from_user.id), whos_rating=int(user_id), rating=int(rating))
            await callback.message.delete()
            if user_lang == 'uz':
                await callback.message.answer("Raiting:{rating}. \nRahmat".format(rating=rating), reply_markup=await orqaga_keyboard(direction, user_lang))
            if user_lang == 'ru':
                await callback.message.answer("Рейтинг:{rating}. \nСпасибо".format(rating=rating), reply_markup=await orqaga_keyboard(direction, user_lang))
            if user_lang == 'en':
                await callback.message.answer("Raiting:{rating}. \nThank you.".format(rating=rating), reply_markup=await orqaga_keyboard(direction, user_lang))

    else:
        await callback.message.delete()
        if user_lang == 'uz':
            await callback.message.answer("O'zingizga raiting qo'ymasligingiz kerak!\n Raiting qabul qilinmadi!", reply_markup=await orqaga_keyboard(level,user_lang))
        if user_lang == 'ru':
            await callback.message.answer("Вы не должны оценивать себя!\n Оценка не принята!", reply_markup=await orqaga_keyboard(level,user_lang))
        if user_lang == 'en':
            await callback.message.answer("You should not put a rating on yourself!\n Rating not accepted!", reply_markup=await orqaga_keyboard(level,user_lang))

    

async def del_user_rating(callback: CallbackQuery, whos_rating, direction, **kwargs):
    await delete_user_rating(callback.from_user.id, whos_rating)
    usrln = await get_user_lang(callback.from_user.id)

    await callback.message.delete()
    if usrln == 'uz':
        await bot.send_message(chat_id = chat_id, text =_("Qanday xizmat ko'rsatishga fikr qoldirasiz?"), reply_markup=direction_button_uz)
    elif usrln == 'en':
        await bot.send_message(chat_id = chat_id, text =_("What kind of service would you like to offer?"), reply_markup=direction_button_en)
    else:
        await bot.send_message(chat_id = chat_id, text =_("На какую обслуживание хотите оставить отзыв"), reply_markup=direction_button_ru)
    
    await ToRating.direction.set()
 




@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """

    :param call: Тип объекта CallbackQuery, который прилетает в хендлер
    :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
    """
    usrln = await get_user_lang(call.from_user.id)

    current_level = callback_data.get("level")
    direction = callback_data.get("direction")
    user_lang = callback_data.get("lang")


    user_id = callback_data.get("user_id")

    rating = callback_data.get("rating")

    whos_rating = int(callback_data.get("whos_rating"))
    print('This call back data '*3)
    print(callback_data)
    levels = {
        "0": users_choice,  
        "1": list_rayting,  
        "2": add_user_rating,
        "3" :del_user_rating
    }
    if current_level == '4':
        await call.message.delete()
        if usrln == 'uz':
            await bot.send_message(chat_id = chat_id, text =_("Qanday xizmat ko'rsatishga fikr qoldirasiz?"), reply_markup=direction_button_uz)
        elif usrln == 'en':
            await bot.send_message(chat_id = chat_id, text =_("What kind of service would you like to offer?"), reply_markup=direction_button_en)
        else:
            await bot.send_message(chat_id = chat_id, text =_("На какую обслуживание хотите оставить отзыв"), reply_markup=direction_button_ru)
        

        await ToRating.direction.set()
    else:

        current_level_function = levels[current_level]

        await current_level_function(
            call,
            user_id=user_id,
            rating=rating,
            level=int(current_level),
            whos_rating=whos_rating,
            direction=direction
        )

@dp.message_handler(user_id=admin_id, state="*", commands=["statistika"])
async def get_stat(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("yil? / year? / Год?")
    await Statistic.year.set()

@dp.message_handler(user_id=admin_id, state=Statistic.year)
async def post_year(message: types.Message, state: FSMContext):
    year = message.text
    if year.isdigit():
        await state.update_data(year=year)
    else:
        await Statistic.year.set()
    await message.answer("oy? / month? / Месяц?")
    await Statistic.month.set()

@dp.message_handler(user_id=admin_id, state=Statistic.month)
async def post_month(message: types.Message, state: FSMContext):
    month = message.text
    if month.isdigit() and int(month) > 0 and int(month) < 13:
        pass
    else:
        Statistic.month.set()
    data = await state.get_data()
    year = data.get("year")
    text = ''
    users = await get_all_users()
    for k, i in enumerate(users):
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        sum_rating = 0
        count = 0
        name = i['full_name']
        user_given_rats = await get_user_given_raitings(int(i['user_id']))
        for j in user_given_rats:
            if j['date'].split('-')[1]==month and j['date'].split('-')[0] == year:
                if int(j['rating'])==1:
                    one += 1
                elif int(j['rating'])==2:
                    two += 1
                elif int(j['rating'])==3:
                    three += 1
                elif int(j['rating'])==4:
                    four += 1
                elif int(j['rating'])==5:
                    five += 1
                sum_rating += int(j['rating'])
                count +=1
        if count == 0:
            arf = 0
        else:
            arf = round(sum_rating/count, 1)
        text+=f'{k+1}) {name} 📊{arf} \n1😣-{one}\n2☹-{two}\n3😕-{three}\n4😑-{four}\n5😍-{five}\n------------\n'
    await message.answer(text)



@dp.message_handler(user_id=admin_id, commands=["add_user"], state="*")
async def add_user_state(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("yangi user IDsini kiriting")
    await AddUser.user_id.set()


@dp.message_handler(user_id=admin_id, state=AddUser.user_id)
async def enter_user_id(message: types.Message, state: FSMContext):
    user_id = message.text
    dic['user_id'] = user_id
    a = await get_user(dic['user_id'])
    print(a)
    await message.answer(f'{a} rasmini kiriting:')
    await AddUser.photo_id.set()


@dp.message_handler(user_id=admin_id, state=AddUser.photo_id, content_types=types.ContentType.PHOTO)
async def add_photo(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await add_photo_to_user(dic['user_id'], photo_id)
    await message.answer_photo(photo=photo_id, caption="Thank you /add_user")
    await state.finish()


@dp.message_handler(user_id=admin_id, state=AddUser, commands=['cancel'])
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("cancelled")
    await state.reset_state()


