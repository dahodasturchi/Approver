from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart(), chat_type = 'private')
async def bot_start(message: types.Message):
    text = "Botni shaxsiy kanalingiz yoki guruhingizga admin qiling."
    text += "Bot kanal yoki guruhingizga kelgan qo'shilish so'rovlarini avtomatik qabul qiladi. Sizga ish qoldirmaydi."
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer(text=text)
    db.add_user(
        user_id= message.from_user.id,
        full_name= message.from_user.full_name,
        lang_code= message.from_user.language_code,
        username= message.from_user.username
    )


@dp.message_handler(commands=["get_database"])
async def get_database(message: types.Message):
    with open(db.db_file_path, 'rb') as file:
        await message.answer_document(document= file)
