from aiogram import Router
from aiogram.filters import Command
from config import bot, admin
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from db.database import sql_command_all_groups_title
from keyboard.reply import admin_kb

router = Router()


@router.message(Command('start'))
async def start(message: Message):
    ADMIN = await admin()
    if message.from_user.id not in ADMIN and message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Данный бот доступен только для администраторов Terra!")
    elif message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Добро пожаловать!\n'
                                                     'Чтобы ознокомиться с ботом, введите команду /help',
                                                     reply_markup=admin_kb)


@router.message(Command('help'))
async def start(message: Message):
    ADMIN = await admin()
    if message.from_user.id not in ADMIN and message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Данный бот доступен только для администраторов Terra!")
    elif message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Чтобы рассылать сообщения с помощью этого бота, для начала нужно'
                                                     ' добавить бота в группы в которые должна приходить рассылка, и '
                                                     'выдать ему там права администратора, после с помощью команды'
                                                     ' /add_group добавить группы в базу данных бота.\n\n'
                                                     'Чтобы разослать сообщение в группы которые вы добавили, нужно'
                                                     ' ввести команду /send_message\n\n'
                                                     'Чтобы удалить группы в которые больше не нужно '
                                                     'рассылать сообщения, введите команду /del_group')


@router.message(Command('del_group'))
async def delete_group(message: Message):
    ADMIN = await admin()
    if message.from_user.id not in ADMIN and message.chat.type == 'private':
        await message.answer("Данный бот доступен только для администраторов Terra!")
    elif message.chat.type == 'private':
        groups = await sql_command_all_groups_title()
        for group in groups:
            keyboard_buttons = [
                [InlineKeyboardButton(text="Удалить", callback_data=f"delete_group {group}")]
            ]
            reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
            await bot.send_message(message.from_user.id, f'{group}',
                                   reply_markup=reply_markup)
