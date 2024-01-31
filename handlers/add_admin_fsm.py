from config import bot, SUPERUSER
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import AddAdmin
from keyboard.reply import admin_add_kb, cancel, admin_kb
from db.database import sql_command_insert_users

router = Router()


@router.message(Command('add_admin'))
async def add_admin(message: Message, state: FSMContext):
    if message.from_user.id not in SUPERUSER and message.chat.type == 'private':
        await message.answer("Доступно только для глав. админов!")
    elif message.chat.type == 'private':
        await state.set_state(AddAdmin.admin)
        await bot.send_message(message.from_user.id, 'Чтобы назначить кого то админом,'
                                                     ' нажмите "Отправить пользователя"', reply_markup=admin_add_kb)


@router.message(AddAdmin.admin)
async def admin_save(message: Message, state: FSMContext):
    if message.user_shared:
        await state.update_data(admin=str(message.user_shared.user_id))
        await bot.send_message(message.from_user.id, 'Укажите ФИО Админа',
                               reply_markup=cancel)
        await state.set_state(AddAdmin.name)
    else:
        await bot.send_message(message.from_user.id, "Отправьте пользователя которого хотите сделать админом!")


@router.message(AddAdmin.name)
async def admin_name(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(name=message.text)
        data = await state.get_data()
        admin_id = data.get('admin')
        admin_name = data.get('name')
        await sql_command_insert_users(admin_id, admin_name)
        await bot.send_message(message.from_user.id, "Админ добавлен!", reply_markup=admin_kb)
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, "Укажите ФИО админа!")
