from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from .routers import film_router

load_dotenv()

root_router = Router()
root_router.include_router(film_router)

@root_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    welcome_message = (
        f"Hello, {hbold(message.from_user.full_name)}!\n"
        "Type /help for a command list"
    )
    await message.answer(welcome_message)
    await message.answer("Join this channel, so you can watch movies inside telegram:")
    await message.answer("https://t.me/+y1ExVET_KTY3MjZi")

@root_router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    help_message = (
        "Available commands:\n"
        "/start - Start\n"
        "/films - Show film list\n"
        "/help - Help message\n"
        "/filmcreate - Add new film\n"
    )
    await message.answer(help_message)

async def main() -> None:
    TOKEN = getenv("BOT_TOKEN")
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_router(root_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
