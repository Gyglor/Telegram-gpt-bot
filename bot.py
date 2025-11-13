import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from openai import OpenAI
from dotenv import load_dotenv

# Загружаем токены
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
openai = OpenAI(api_key=OPENAI_API_KEY)

# Команда /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я бот на базе GPT. Отправь мне сообщение, и я отвечу.")

# Все остальные текстовые сообщения
@dp.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    if message.text.startswith('/'):
        # Игнорируем другие команды
        return
        await bot.send_chat_action(message.chat.id, action="typing")

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ты полезный ассистент в Telegram."},
                {"role": "user", "content": message.text},
            ],
            max_tokens=800,
            temperature=0.2,
        )
        answer = response.choices[0].message.content
        await message.reply(answer)
    except Exception as e:
        await message.reply(f"Ошибка при обращении к OpenAI: {e}")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
