from aiogram.types import Message, CallbackQuery
from aiogram import F
from keyboards.inline.productsKeyboard import mahsulotlar

from loader import dp

@dp.message(F.text == "Mahsulotlar")
async def product_handler(message: Message):
    await message.answer("Quyidagi mahsulotlar mavjud:", reply_markup=mahsulotlar)


@dp.callback_query(lambda query: query.data.startswith("product"))
async def product_queryHandler(query: CallbackQuery):
    await query.answer(cache_time=10)
    product = query.data.split(":")[1]
    if product == "televizor":
        await query.message.answer_photo(photo="https://img.etimg.com/photo/msid-101298876,imgsize-68456/OnePlus32-inchYSeriesHDReadyLEDSmartTV.jpg", caption="Brand: OnePlus\n Rangi: qora,\n O'lchami: 52'\nNarxi: 500$")
    elif product == "konditsioner":
        await query.message.answer(text="Yangi katta konditsioner\nNarxi: 400$")
    elif product == "muzlatgich":
        await query.message.answer(text="Ikkita xonalik katta muzlatgich\n Narxi: 350$")