from aiogram import Router
from aiogram.filters import Command
from config import bot, SUPERUSER
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from db.database import sql_command_all_users_name

router = Router()


@router.message(Command('del_admin'))
async def delete_admin(message: Message):
    if message.from_user.id not in SUPERUSER and message.chat.type == 'private':
        await message.answer("Доступно только для глав. админов!")
    elif message.chat.type == 'private':
        users = await sql_command_all_users_name()
        for user in users:
            keyboard_buttons = [
                [InlineKeyboardButton(text=f"Удалить", callback_data=f"delete_user {user}")]
            ]
            reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
            await bot.send_message(message.from_user.id, f'{user}',
                                   reply_markup=reply_markup)

