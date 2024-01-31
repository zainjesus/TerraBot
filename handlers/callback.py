from aiogram.types import CallbackQuery
from config import bot
from db.database import sql_command_delete_users, sql_command_delete_groups
from aiogram import Router, F


router = Router()


@router.callback_query(F.data.startswith("delete_user "))
async def complete_delete(call: CallbackQuery):
    await sql_command_delete_users(call.data.replace('delete_user ', ''))
    await call.answer(text="Админ удален", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


@router.callback_query(F.data.startswith("delete_group "))
async def complete_delete(call: CallbackQuery):
    await sql_command_delete_groups(call.data.replace('delete_group ', ''))
    await call.answer(text="Группа удалена", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)
