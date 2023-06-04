import json

from aiogram import Bot
from aiogram.types import Message

from telebot.core.config.settings import settings
from telebot.core.utils.comands import set_commands
from telebot.core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard

from telebot.core.keyboards.inline import select_macbook, get_inline_keyboard


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Привет {message.from_user.first_name}. Рад тебя видеть!</b>', reply_markup=get_reply_keyboard())
    # await message.answer(f'<s>Привет {message.from_user.first_name}. Рад тебя видеть!</s>', reply_markup=reply_keyboard)
    # await message.reply(f'<tg-spoiler>Привет {message.from_user.first_name}. Рад тебя видеть!</tg-spoiler>')


async def get_location(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Ты отправил локацию!\r\a'
                                                 f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_inline(message: Message, bot: Bot):
    await message.answer(f"Привет, {message.from_user.first_name}. Показываю инлайн кнопки!",
                         reply_markup=get_inline_keyboard())  # -> reply_markup=select_macbook


async def get_photo(message: Message, bot: Bot):
    await message.answer('Отлично! Ты отправил картинку, я сохраню её себе.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'core/media/img/photo.png')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
