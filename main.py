import telebot
from telebot import types
from key_value import *

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    start_message = f'''<b>Привет Герой !!!</b>\nЕсли ты готов играть, жми <b>GO</b> и поехали!'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items1 = types.KeyboardButton("Go")
    markup.add(items1)
    bot.send_message(message.chat.id, start_message,
                     reply_markup=markup, parse_mode='html')


bot.infinity_polling()
