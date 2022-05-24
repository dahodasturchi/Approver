from aiogram import types



from loader import dp, bot, db


@dp.chat_join_request_handler()
async def acceptRequest(message: types.Message):
    try:
        chat_id = message.chat.id
        user = message.from_user.id
        await bot.approve_chat_join_request(
            chat_id,
            user
        )
        if message.chat.username:
            username = message.chat.username
        db.add_chat(
            chat_id= chat_id,
            chat_title= message.chat.title,
            chat_type= message.chat.type,
            username= username
        )
    except Exception as e:
        print("ERROR in channel handler", e)
    