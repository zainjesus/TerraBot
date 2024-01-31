from aiogram import Router
from config import bot, admin
from aiogram.types import Message

router = Router()


@router.message()
async def extra(message: Message):
    ADMIN = await admin()
    if message.from_user.id not in ADMIN and message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Данный бот доступен только для администраторов Terra!")
    elif message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Такой команды нет!")
