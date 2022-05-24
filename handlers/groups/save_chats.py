from aiogram import types

from loader import dp, db 


@dp.message_handler(chat_type= ['group','supergroup'])
async def save_chat_data(message: types.Message):
    db.add_chat(
        chat_id= message.chat.id,
        chat_title= message.chat.title,
        chat_type= message.chat.type,
        username= message.chat.username
    )