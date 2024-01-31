from config import bot, admin
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import AddGroup
from keyboard.reply import group_add_kb, cancel, admin_kb
from db.database import sql_command_insert_groups

router = Router()


@router.message(Command('add_group'))
async def add_group(message: Message, state: FSMContext):
    ADMIN = await admin()
    if message.from_user.id not in ADMIN and message.chat.type == 'private':
        await message.answer("Данный бот доступен только для администраторов Terra!")
    elif message.chat.type == 'private':
        await state.set_state(AddGroup.group)
        await bot.send_message(message.from_user.id, 'Чтобы добавить группу, нажмите "Отправить группу"',
                               reply_markup=group_add_kb)


@router.message(AddGroup.group)
async def group_save(message: Message, state: FSMContext):
    if message.chat_shared:
        await state.update_data(group=str(message.chat_shared.chat_id))
        await bot.send_message(message.from_user.id, 'Укажите название группы\n(Необязательно точь в точь, '
                                                     'главное чтобы было понятно, что это за группа)',
                               reply_markup=cancel)
        await state.set_state(AddGroup.title)
    else:
        await bot.send_message(message.from_user.id, "Отправьте группу которую хотите добавить!")


@router.message(AddGroup.title)
async def group_name(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(title=message.text)
        data = await state.get_data()
        group_id = data.get('group')
        group_title = data.get('title')
        await sql_command_insert_groups(group_id, group_title)
        await bot.send_message(message.from_user.id, "Группа добавлена!", reply_markup=admin_kb)
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, "Укажите название группы!!")

        
