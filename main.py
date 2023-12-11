
from db_graphics.GraphicsController import MainGraphic, WarriorStory
from telebot import types
from temp_token import my_token
import telebot


bot = telebot.TeleBot((my_token()), parse_mode='html')


@bot.message_handler(commands=['start'])
def start(message):

    start_message: str = f'<b>Привет Герой !!!</b> \n Если ты готов играть, жми GO и поехали!'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items1 = types.KeyboardButton("Go")
    markup.add(items1)
    bot.send_message(message.chat.id, start_message,
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types="text")
def message_replay(message):
    if message.text == "Go":
        text_mes: str = f"<b>DUNGEON OF SHADOWS</b> подарит тебе мир, полный тайн и волшебства. " \
            f"Пройдя до конца путь сражений и разгадав все загадки," \
            f"\nты изменишься… или просто повеселишься 🔥🔥🔥. " \
            f"\n" \
            f"\n<b>Теперь пришло время выбрать Героя!</b>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        warrior = types.KeyboardButton('Воин')
        mage = types.KeyboardButton('Чародей')
        hunt = types.KeyboardButton('Охотник')
        markup.add(warrior, mage, hunt)
        bot.send_photo(message.chat.id, MainGraphic.main_image())
        bot.send_message(message.chat.id, text_mes,
                         reply_markup=markup, parse_mode='html')

    elif message.text == 'Воин':
        bot.send_message(
            message.chat.id, '<b>🗡Ты выбрал воина - круто!🗡</b>', parse_mode='html')
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_game = types.KeyboardButton(text="Начать играть за Война")
        bt_help = types.KeyboardButton(text="Правила игры")
        keyboard.add(bt_game, bt_help)
        bot.send_photo(message.chat.id, MainGraphic.main_warrior())
        bot.send_message(message.chat.id, "<i>Перед началом игры \nможно ознакомся с правилами.\nЛибо пропустить.</i>",
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == "Начать играть за Война":
        text_warrior_01 = "Ты знатный воин и любимец женщин.\nВозвращаясь с охоты, гордый собой,\nты увидел старца, медитирующего на берегу реки."
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text="Задать вопрос старцу")
        keyboard.add(bt_warrior_1)
        bot.send_photo(message.chat.id, WarriorStory.old_man_001())
        bot.send_message(message.chat.id, text_warrior_01,
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == 'Задать вопрос старцу':
        text_warrior_2 = "Эй, старик, чем ты занят? Что же ты молчишь?"
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt_warrior_2 = types.KeyboardButton(text="Старик молчал")
        keyboard.add(bt_warrior_2)
        bot.send_message(message.chat.id, text_warrior_2,
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == "Старик молчал":
        text_warrior_03 = "Старец, погруженный в транс, не ответил тебе. Ты видишь мертвую змею, лежащую неподалёку.\n"
        "Подцепив её кончиком кинжала, решаешь подшутить над старцем."
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_warrior_3 = types.KeyboardButton(text="Повесить змею старцу на шею")
        keyboard.add(bt_warrior_3)
        bot.send_message(message.chat.id, text_warrior_03,
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == "Повесить змею старцу на шею":
        text_warrior_01 = "Уйти в свой замок"
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text=text_warrior_01)
        keyboard.add(bt_warrior_1)
        bot.send_message(message.chat.id, "Довольный собой и своей шуткой, уходишь. ",
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == "Уйти в свой замок":
        text_warrior = "Кажется, сегодня боги отвернулись от тебя. Выйдя из транса, старец с помощью внутреннего взора без труда увидел, кто подшутил над ним, и разгневался."
        text_warrior_01 = "Продолжить"
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text=text_warrior_01)
        keyboard.add(bt_warrior_1)

        bot.send_photo(message.chat.id, WarriorStory.old_man_002())
        bot.send_message(message.chat.id, text_warrior,
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == 'Продолжить':
        text_warrior = "О, знатный воин! ты слишком гордишься своим положением и забыл, \n "
        'что такое уважение. За это я проклинаю тебя! Ты потеряешь свое богатство и будешь скитаться, покинутый всеми!'

        text_warrior_01 = "Продолжить"
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text=text_warrior_01)
        keyboard.add(bt_warrior_1)
        bot.send_message(message.chat.id, text_warrior,
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == 'Продолжить':
        text_warrior = "В тот же миг твои замки вспыхнули, и только несколько слуг смогли спастись из огня. Твоя семья погибла, а на самого тебя напали лютые бандиты. Bзраненный, "
        "ты бросаешься в реку и, ухватившись за бревнышко, плывешь вниз по течению. вскоре тебя спасают рыбаки, и ты узнаешь, что случилось с твоими замками и семьей."

        text_warrior_01 = "Продолжить"
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text=text_warrior_01)
        keyboard.add(bt_warrior_1)
        bot.send_message(message.chat.id, text_warrior, parse_mode='html')

###################################################################################################################################################

    elif message.text == 'Чародей':
        bot.send_message(
            message.chat.id, '<b>🔮Ты выбрал Чародейку - круто!🔮</b>', parse_mode='html')
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_game = types.KeyboardButton(text="Начать играть")
        bt_help = types.KeyboardButton(text="Правила игры")
        bt_next = types.KeyboardButton(text="Пропустить")
        keyboard.add(bt_game, bt_help, bt_next)
        bot.send_photo(message.chat.id, MainGraphic.main_magic())
        bot.send_message(message.chat.id,
                         "<i>Перед началом игры \nможно ознакомся с правилами.\nЛибо пропустить.</i>",
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == 'Охотник':
        bot.send_message(
            message.chat.id, '<b>🏹Ты выбрал Охотника - круто!🏹</b>', parse_mode='html')
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)
        bt_game = types.KeyboardButton(text="Начать играть")
        bt_help = types.KeyboardButton(text="Правила игры")
        bt_next = types.KeyboardButton(text="Пропустить")
        keyboard.add(bt_game, bt_help, bt_next)
        bot.send_video(message.chat.id, MainGraphic.main_hunter())
        bot.send_message(message.chat.id,
                         "<i>Перед началом игры \nможно ознакомся с правилами.\nЛибо пропустить.</i>",
                         reply_markup=keyboard, parse_mode='html')


class PrologWarrior:
    @bot.message_handler(content_types="text")
    def message_replay(message):
        if message.text == "Начать играть" or "Пропустить":
            bot.send_message(
                message.chat.id, '<b>Игра началась!</b>', parse_mode='html')


try:
    # Запуск бота
    if __name__ == '__main__':
        bot.polling(none_stop=True)
        bot.infinity_polling()
except:
    print('Ошибка запуска бота!')
