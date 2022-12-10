# from main import dp
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types

# res = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] # будущие элементы вашей инлайн клавы, не надо их импортировать через global, это просто пример списка чтоб компилятор не ругался
# PAGE_SIZE = 3 # по сколько выводить в самой клаве



# async def answer_with_menu(message: types.Message, state: FSMContext, menu_page_shift: int):
#     global res
#     async with state.proxy() as data:
#         current_page_index = data['res']
#         new_page_index = current_page_index + menu_page_shift
#         if (new_page_index < 0 or new_page_index > len(res)/PAGE_SIZE):
#             new_page_index = current_page_index
#         data['res'] = new_page_index

#     the_keyboard = InlineKeyboardMarkup()
#     index = new_page_index * PAGE_SIZE
#     for text in res[index:index + PAGE_SIZE]:
#         button = InlineKeyboardButton(text=text, callback_data='the_step')
#         the_keyboard.add(button)
#     next = InlineKeyboardButton(text='Назад', callback_data='back_step')
#     back = InlineKeyboardButton(text='Далее', callback_data='next_step')
#     stop = InlineKeyboardButton(text='Закончить просмотр', callback_data='stop')
#     the_keyboard.row(next, back).add(stop)

#     await message.answer('Меню', reply_markup=the_keyboard)


# @dp.message_handler(text='/test', state='*')
# async def enter_test(message: types.Message, state: FSMContext):
#     await Menu.step.set()
#     async with state.proxy() as data:
#         data['res'] = 0
#     await answer_with_menu(message, state, 0)


# @dp.callback_query_handler(text='next_step', state=Menu.step)
# async def next_menu(callback: types.CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await answer_with_menu(callback.message, state, +1)


# @dp.callback_query_handler(text='back_step', state=Menu.step)
# async def back_menu(callback: types.CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await answer_with_menu(callback.message, state, -1)


# @dp.callback_query_handler(text='stop', state=Menu.step)
# async def newk_sui3(callback: types.CallbackQuery, state: FSMContext):
#     await callback.message.delete()
#     await callback.message.answer('Подбор закончен')
#     await state.finish()