from openai import OpenAI
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Простой запрос к модели
response = client.chat.completions.create(
    model="gpt-4o",  # если GPT-5 недоступна
    messages=[{"role": "user", "content": "Привет!"}]
)

print(response.choices[0].message.content)
