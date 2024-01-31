import asyncio
from config import dp, bot
from handlers import extra, admin, distribution_fsm, superuser, callback, add_admin_fsm, add_group_fsm
from utils import common
import logging
from db.database import sql_create


async def main():
    sql_create()
    dp.include_routers(
        admin.router,
        common.router,
        distribution_fsm.router,
        superuser.router,
        callback.router,
        add_admin_fsm.router,
        add_group_fsm.router,
        extra.router

    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

    