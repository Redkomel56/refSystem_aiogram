from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import IsUser

from loader import dp


@dp.message_handler(IsUser(), Command('about'))
async def about(message: types.Message):
    text = """Бот создан для статьи, чтобы показать возможности языка программирования Python"""
    await message.answer(text=text)