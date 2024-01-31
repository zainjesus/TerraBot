from aiogram import Bot, Dispatcher
from decouple import config
from db.database import sql_command_all_users, sql_command_all_groups

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher()


async def admin():
    ADMIN = await sql_command_all_users()
    DEFAULT_ADMIN = [517935907, 167495608, 465483170, 415378588, 989897530]
    ADMIN += DEFAULT_ADMIN
    return ADMIN


async def group():
    GROUP = await sql_command_all_groups()
    return GROUP


SUPERUSER = [517935907, 167495608, 465483170, 415378588, 989897530]
