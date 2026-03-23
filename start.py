"""
start.py — запускает бота и FastAPI одновременно
"""
import asyncio
import logging
import uvicorn

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN, USD_KZT_RATE, CASHBACK_PERCENT, DATABASE_INTERNAL_URL, DATABASE_PUBLIC_URL
from db import init_db, close_pool
from handlers import setup_routers
from api import app as fastapi_app


async def run_bot():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
        datefmt="%H:%M:%S",
    )

    print("\033[35m" + "═" * 58)
    print("  🛍  SHOPBOT — Шымкент, Казахстан")
    print("  🗄  PostgreSQL (asyncpg) + aiogram 3.x")
    print("═" * 58 + "\033[0m")
    print(f"  💱 Курс USD/KZT : {USD_KZT_RATE} (фикс.)")
    print(f"  🎁 Кэшбэк       : {CASHBACK_PERCENT}%")
    print(f"  🔌 DB internal  : {DATABASE_INTERNAL_URL}")
    print(f"  🌐 DB public    : {DATABASE_PUBLIC_URL}")
    print()

    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    setup_routers(dp)

    print("\033[32m  🚀 Бот запущен и готов!\033[0m\n")

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await close_pool()
        await bot.session.close()
        print("\033[33m  🛑 Бот остановлен\033[0m")


async def run_api():
    config = uvicorn.Config(
        app=fastapi_app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    # Инициализируем БД один раз для обоих
    await init_db()
    # Запускаем бота и API параллельно
    await asyncio.gather(
        run_bot(),
        run_api(),
    )


if __name__ == "__main__":
    asyncio.run(main())
