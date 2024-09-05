from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuButtons = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Mahsulotlar"),
            KeyboardButton(text="Shaxsiy kabinet")
        ],
        [
            KeyboardButton(text="Biz haqimizda"),
        ]
    ]
)