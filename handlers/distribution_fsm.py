from config import bot, admin, group
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Distribution
from keyboard.reply import distribution_submit, distribution_photo, admin_kb, cancel

router = Router()


@router.message(Command('send_message'))
async def send_message(message: Message, state: FSMContext):
    ADMIN = await admin()
    if message.from_user.id not in ADMIN and message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Данный бот доступен только для администраторов Terra!")
    elif message.chat.type == 'private':
        await state.set_state(Distribution.message)
        await bot.send_message(message.from_user.id, "Введите сообщение, которое хотите разослать", reply_markup=cancel)


@router.message(Distribution.message)
async def message_save(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(message=message.text)
        await bot.send_message(message.from_user.id, 'Если хотите прикрепить к сообщению фотографию, отправьте ее мне\n'
                                                     '(только одно фото)',
                                                     reply_markup=distribution_photo)
        await state.set_state(Distribution.photo)
    else:
        await bot.send_message(message.from_user.id, "На этом этапе можно только ввести текст!")


@router.message(Distribution.photo)
async def photo_save(message: Message, state: FSMContext):
    if message.text == "Оставить без фото":
        await state.set_state(Distribution.submit)
        await bot.send_message(message.from_user.id, 'Чтобы разослать это сообщение, нажмите "ДАЛЕЕ"',
                               reply_markup=distribution_submit)
    elif message.photo:
            await state.update_data(photo=message.photo[-1].file_id)
            await bot.send_message(message.from_user.id, 'Чтобы разослать это сообщение, нажмите "ДАЛЕЕ"',
                                   reply_markup=distribution_submit)
            await state.set_state(Distribution.submit)
    else:
        await bot.send_message(message.from_user.id, "На этом этапе можно только прикрепить фото!")


@router.message(Distribution.submit)
async def submit(message: Message, state: FSMContext):
    if message.text == "ДАЛЕЕ":
        data = await state.get_data()
        user_message = data.get('message')
        user_photo = data.get('photo')
        GROUP = await group()
        await bot.send_message(message.from_user.id, "Сообщение успешно разослано!", reply_markup=admin_kb)
        await state.clear()
        for i in GROUP:
            if user_photo:
                await bot.send_photo(i, photo=user_photo, caption=user_message)
            else:
                await bot.send_message(i, user_message)
    elif message.text == "ОТМЕНИТЬ":
        await bot.send_message(message.from_user.id, "Рассылка отменена!", reply_markup=admin_kb)
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Нажмите "ДАЛЕЕ" или "ОТМЕНИТЬ"', reply_markup=admin_kb)





