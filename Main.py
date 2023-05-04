from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Command

from YTracker import YandexTracker
from YTracker import get_tasks
from config import token, org_id


API_TOKEN = 'hidden'
YT_TOKEN = 'hidden'
YT_USER_ID = 'hidden'

# Configure bot here
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Creating instance of YandexTracker
tracker = YandexTracker(YT_TOKEN)

async def get_issues_command(query):
    issues = tracker.get_issues(YT_USER_ID)
    if issues:
        message = "Список задач:\n\n"
        for issue in issues:
            message += f"- {issue['summary']}\n"
    else:
        message = "У вас нет задач в Яндекс.Трекере."
    await query.message.answer(message)

async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_tasks = types.KeyboardButton(text="Получить список задач")
    keyboard.add(button_tasks)
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(text="Получить список задач")
async def get_tasks_command(message: types.Message):
    tasks = await get_tasks(token, org_id, YT_USER_ID)
    await message.answer(f"Список задач: {tasks}")
    
    
