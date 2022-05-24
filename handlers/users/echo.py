from aiogram import types

from loader import dp


from aiogram.types import InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb

markup = ikm(
    inline_keyboard=[
        [ikb("Guruhga qo'shish ➕", url="https://t.me/joinrequestsbot?startgroup=new")],
        [ikb("Kanalga qo'shish ➕", url="https://t.me/joinrequestsbot?startchannel=new")]
    ]
)



# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Botni guruhlarga qo'shing!!!", reply_markup=markup)
