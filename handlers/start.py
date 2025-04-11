from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.all_kb import main_kb
from aiogram.types import BotCommand, BotCommandScopeDefault

start_router = Router()

async def set_commands():
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='start_2', description='Старт 2'),
                BotCommand(command='start_3', description='Старт 3')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()',
        reply_markup=main_kb(message.from_user.id))

@start_router.message(F.text == '/start_id')
async def cmd_start_3(message: Message):
    await message.answer(str(message.from_user.id))

