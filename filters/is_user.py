from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data import config
from utils import mysql


class IsUser(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        db = mysql.MySQL(
            host=config.HOST_DB,
            port=config.PORT_DB,
            user=config.USER_DB,
            password=config.PASSWORD_DB,
            db_name=config.NAME_DB)
        register = db.check_user_register(message.from_user.id)
        if not register:
            await message.answer('У вас нет доступа к командам, пока вы не зарегистрированы')
        return register