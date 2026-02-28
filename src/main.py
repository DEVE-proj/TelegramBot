from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()

bot = TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id, "Hello!)")

bot.polling()