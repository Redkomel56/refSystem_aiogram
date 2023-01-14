from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import IsUser

from loader import dp, bot
from data import config
from utils import mysql
from keyboards.inline import commands_i
from keyboards.default import commands_d


@dp.message_handler(IsUser(), Command('menu'))
async def menu(message: types.Message):
    await message.answer(text="Вы перешли в меню", reply_markup=commands_d.menu_kb)
    await message.answer(text="Какие-то команды: ", reply_markup=commands_i.commands_kb)


@dp.message_handler(IsUser(), text='Реферальная ссылка')
async def ref(message: types.Message):
    db = mysql.MySQL(
        host=config.HOST_DB,
        port=config.PORT_DB,
        user=config.USER_DB,
        password=config.PASSWORD_DB,
        db_name=config.NAME_DB)
    info = await bot.get_me()
    link = db.get_ref_link(message.from_user.id)
    count = db.get_transitions(link)
    await message.answer(text=f"Ссылка: https://t.me/{info.username}?start={link} | Рефералов: {count}")