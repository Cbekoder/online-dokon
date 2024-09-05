from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mahsulotlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Televizor 52'", callback_data="product:televizor")],
        [InlineKeyboardButton(text="Konditsioner", callback_data="product:konditsioner")],
        [InlineKeyboardButton(text="Muzlatgich", callback_data="product:muzlatgich")]
    ]
)