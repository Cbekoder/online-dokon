from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram import html
from bot.keyboards.default.menuKeyboard import menuButtons

from loader import dp, db

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    id = message.from_user.id
    if not db.select_user(id):
        full_name = message.from_user.full_name
        username = message.from_user.username if message.from_user.username else None
        # phone = message.from_user.phone if message.from_user.phone else None
        db.new_user(id, full_name, username
                    )
    await message.answer(f"Assalomu alaykum, {html.bold(message.from_user.full_name)}!", reply_markup=menuButtons)
