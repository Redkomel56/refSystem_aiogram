from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


commands_kb = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text="Команда 1",
                                                        callback_data="с1"
                                                    ),
                                                    InlineKeyboardButton(
                                                        text="Команда 2",
                                                        callback_data="c2"
                                                    )
                                                ]
                                            ])