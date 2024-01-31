from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonRequestUser, KeyboardButtonRequestChat


admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/help"),
            KeyboardButton(text="/send_message"),
        ],
        [
            KeyboardButton(text="/add_group"),
        ]
    ],
    resize_keyboard=True,
)


admin_add_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить пользователя", request_user=KeyboardButtonRequestUser(
                            request_id=2, user_is_bot=False
            )),
        ],
        [
            KeyboardButton(text='ОТМЕНА')
        ]
    ],
    resize_keyboard=True
)


group_add_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить группу", request_chat=KeyboardButtonRequestChat(
                            request_id=1, chat_is_channel=False
            )),
        ],
        [
            KeyboardButton(text='ОТМЕНА')
        ]
    ],
    resize_keyboard=True
)

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ОТМЕНА')
        ]
    ],
    resize_keyboard=True
)


distribution_submit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ДАЛЕЕ"),
            KeyboardButton(text="ОТМЕНИТЬ")
        ]
    ],
    resize_keyboard=True,
)


distribution_photo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оставить без фото")
        ],
        [
            KeyboardButton(text='ОТМЕНА')
        ]
    ],
    resize_keyboard=True,
)


rmk = ReplyKeyboardMarkup(
    keyboard=[[]]
)
