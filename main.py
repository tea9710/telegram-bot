import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🔹 Вставь свой токен бота
API_TOKEN = "7549509481:AAHmQwtM0z2ClzdAmchrForpnFCIMy1jJn4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Клавиатура
keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True, keyboard=[[KeyboardButton(text="Поиск напарника")], [KeyboardButton(text="Стоп")]]
)

# Команда /start
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Нажми 'Поиск напарника', чтобы начать.", reply_markup=keyboard)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
