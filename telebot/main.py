from aiogram import Bot, Dispatcher, F

from aiogram.types import ContentType
from aiogram.filters import ContentTypesFilter, Command, CommandStart

from core.filters.iscontact import IsTrueContact

from telebot.core.handlers.base import get_start, start_bot, stop_bot, get_photo, get_hello
from telebot.core.handlers.contact import get_true_contact, get_fake_contact

import asyncio
import logging

from telebot.core.config.settings import settings


async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - &(name)s - "
                                                   "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_true_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]), IsTrueContact())
    dp.message.register(get_fake_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]))
    # dp.message.register(get_photo, ContentTypesFilter(content_types=[ContentType.PHOTO]))
    dp.message.register(get_photo, F.photo)
    # dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
