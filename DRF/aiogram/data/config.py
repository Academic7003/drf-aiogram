from decouple import config
from pathlib import Path

BOT_TOKEN = str(config('BOT_TOKEN'))

# Заберем данные для подключения к базе данных (юзер, пароль, название бд) - тоже прописать в файле ".env"
# PGUSER = str(config("PGUSER"))
# PGPASSWORD = str(config("PGPASSWORD"))
# DATABASE = str(config("DATABASE"))

admins = [
    config("ADMIN_ID"),
    config('ADMIN_ID2')
]

ip = config("ip")

# Ссылка подключения к базе данных
# POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
I18N_DOMAIN = 'hayatbot'
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'
print(BASE_DIR)