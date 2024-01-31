from aiogram.fsm.state import StatesGroup, State


class Distribution(StatesGroup):
    message = State()
    photo = State()
    submit = State()


class AddAdmin(StatesGroup):
    admin = State()
    name = State()


class AddGroup(StatesGroup):
    group = State()
    title = State()
