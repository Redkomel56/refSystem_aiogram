import asyncio
import logging

from aiogram import executor

from loader import dp, bot
import filters, handlers
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Удаляем сообщения, которые пришли пока бот был выключен
    await bot.delete_webhook(drop_pending_updates=True)

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

