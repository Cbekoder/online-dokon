from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F

from loader import dp, db

@dp.message(F.text == "Shaxsiy kabinet")
async def profile(message: Message):
    user = db.select_user(message.from_user.id)[0]
    if user:
        await message.answer(f"Ism: {user.name},\nid: {user.id}, \nusername: {user.username}, Phone number: {user.phone}")


@dp.message(F.text == "Biz haqimizda")
async def info(message: Message):
    links = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram", url="https://t.me/cbekoder")
        ]
    ])
    await message.answer("Biz bilan aloqa:", reply_markup=links)