from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import os
from api.api import Api
import asyncio

load_dotenv()

bot = AsyncTeleBot("")

@bot.message_handler(commands=['news'])
async def start(message):

    news = await Api.get_all_posts()

    for post in news:

        await bot.send_message(message.chat.id, post)

if __name__ == "__main__":

    asyncio.run(bot.polling())