from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from data import config
from utils import mysql


def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    db = mysql.MySQL(
        host=config.HOST_DB,
        port=config.PORT_DB,
        user=config.USER_DB,
        password=config.PASSWORD_DB,
        db_name=config.NAME_DB)
    invited_code = extract_unique_code(message.text)
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\nЭто бот был создан для стать на сайте directprobi.ru\nНапишите комманду \help чтобы получить подробную информацию о возможнастях бота")
    if not db.check_user_register(message.from_user.id):
        db.add_user(message.from_user.id, message.from_user.username, invited_code)
        await message.answer(f"Создал вам учетную запись в базе данных")
    else:
        await message.answer(f"Вы уже зарегистрированы")

