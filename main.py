
from telebot import types
from db_img.GraphicsController import *
from temp_token import my_token
import telebot


bot = telebot.TeleBot((my_token()), parse_mode='html')


@bot.message_handler(commands=['start'])
def start(message):

    start_message : str = f'<b>Привет Герой !!!</b> \n Если ты готов играть, жми GO и поехали!'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items1 = types.KeyboardButton("Go")
    markup.add(items1)
    bot.send_message(message.chat.id, start_message, reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types="text")
def message_replay(message):
    if message.text == "Go":
        text_mes : str = f"<b>DUNGEON OF SHADOWS</b> подарит тебе мир, полный тайн и волшебства. " \
                   f"Пройдя до конца путь сражений и разгадав все загадки," \
                   f"\nты изменишься… или просто повеселишься 🔥🔥🔥. " \
                   f"\n" \
                   f"\n<b>Теперь пришло время выбрать Героя!</b>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        warrior = types.KeyboardButton('Воин')
        mage = types.KeyboardButton('Чародей')
        hunt = types.KeyboardButton('Охотник')
        markup.add(warrior, mage, hunt)
        
        bot.send_photo(message.chat.id, main_image())
        bot.send_message(message.chat.id, text_mes, reply_markup=markup, parse_mode='html')

    elif message.text == 'Воин':
        bot.send_message(message.chat.id, '<b>🗡Ты выбрал воина - круто!🗡</b>', parse_mode='html')
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt_game = types.KeyboardButton(text="Начать играть")
        bt_help = types.KeyboardButton(text="Правила игры")
        bt_next = types.KeyboardButton(text="Пропустить")
        keyboard.add(bt_game, bt_help, bt_next)
        bot.send_video(message.chat.id, main_warrior())
        bot.send_message(message.chat.id,
                         "<i>Перед началом игры \nможно ознакомся с правилами.\nЛибо пропустить.</i>",
                         reply_markup=keyboard, parse_mode='html')









if __name__ == "__main__":
    bot.polling(none_stop=True)
    bot.infinity_polling()
