# from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types
# from data.config import I18N_DOMAIN, LOCALES_DIR
from utils.db_api.db_commands import *



# async def get_lang(user_id):
#     user = await get_ratinger(user_id)
#     print(user)
#     if user:
#         return user['language']


# class ACLMiddleware(I18nMiddleware):
#     async def get_user_locale(self, action, args):
#         user = types.User.get_current()
#         print(user.locale, 7777777777777777777777777777777777)
#         if await get_lang(user.id):
#             return await get_lang(user.id) 
#         else:
#             return user.locale  

# def setup_middleware(dp):
#     i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
#     dp.middleware.setup(i18n)
#     return i18n
