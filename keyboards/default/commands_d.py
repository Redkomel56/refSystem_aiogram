from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Переход 1")
    ],
    [
        KeyboardButton(text="Действие 1"),
        KeyboardButton(text="Дествие 2")
    ],
    [
        KeyboardButton(text="Реферальная ссылка")
    ]
], resize_keyboard=True)