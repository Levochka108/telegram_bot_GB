
from db_graphics.GraphicsController import MainGraphic, WarriorStory
from telebot import types
from temp_token import my_token
import telebot
import logging

FILENAME = 'logs/game_log.log'
FORMAT = '%(asctime)s [%(levelname)s]: %(message)s'
ENCODING = "utf-8"
logging.basicConfig(filename=FILENAME, level=logging.INFO,
                    format=FORMAT, encoding=ENCODING)


bot = telebot.TeleBot((my_token()), parse_mode='html')
user_states = {}


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

    user_state = user_states.get(message.chat.id, None)

    # Пример логирования
    logging.info(
        f"User {message.from_user.username} with ID {message.from_user.id} sent a message: {message.text}")

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
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt_game = types.KeyboardButton(text="Начать играть за Война")
        bt_help = types.KeyboardButton(text="Правила игры")
        keyboard.add(bt_game, bt_help)
        bot.send_photo(message.chat.id, MainGraphic.main_warrior())
        bot.send_message(message.chat.id, "<i>Перед началом игры \nможно ознакомиться с правилами.\nЛибо пропустить.</i>",
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == "Начать играть за Война":
        text_warrior_01 = "Ты знатный воин и любимец женщин.\nВозвращаясь с охоты, гордый собой,\nты увидел старца, медитирующего на берегу реки."
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
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
        text_warrior_03 = "Старец, погруженный в транс, не ответил тебе. Ты видишь мертвую змею, лежащую неподалёку.\n" \
            "Подцепив её кончиком кинжала, решаешь подшутить над старцем."
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt_warrior_3 = types.KeyboardButton(text="Повесить змею старцу на шею")
        keyboard.add(bt_warrior_3)
        bot.send_message(message.chat.id, text_warrior_03,
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == "Повесить змею старцу на шею":
        text_warrior_01 = "Уйти в свой замок"
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text=text_warrior_01)
        keyboard.add(bt_warrior_1)
        bot.send_message(message.chat.id, "Довольный собой и своей шуткой, уходишь. ",
                         reply_markup=keyboard, parse_mode='html')

    elif message.text == "Уйти в свой замок":
        text_warrior = "Кажется, сегодня боги отвернулись от тебя. Выйдя из транса, старец с помощью внутреннего взора без труда увидел, кто подшутил над ним, и разгневался."
        text_warrior_01 = "Продолжить"
        user_states[message.chat.id] = 'continue_state'

        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text=text_warrior_01)
        keyboard.add(bt_warrior_1)
        bot.send_photo(message.chat.id, WarriorStory.old_man_002())
        bot.send_message(message.chat.id, text_warrior,
                         reply_markup=keyboard, parse_mode='html')

    elif user_states.get(message.chat.id) == 'continue_state' and message.text == 'Продолжить':
        # Обработка продолжения после "Уйти в свой замок"
        text_warrior = "— О, знатный воин! \nТы слишком гордишься своим положением и забыл," \
            " что такое уважение. За это я проклинаю тебя! Ты потеряешь свое богатство и будешь скитаться, покинутый всеми!"
        user_states.pop(message.chat.id)

        user_states[message.chat.id] = 'continue_state_1'
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text="Продолжить")
        keyboard.add(bt_warrior_1)
        bot.send_message(message.chat.id, text_warrior,
                         reply_markup=keyboard, parse_mode='html')

    elif user_states.get(message.chat.id) == 'continue_state_1' and message.text == 'Продолжить':
        text_warrior = "В тот же миг твои замки вспыхнули, и только несколько слуг смогли спастись из огня. Твоя семья погибла, а на самого тебя напали лютые бандиты. Bзраненный, " \
            "ты бросаешься в реку и, ухватившись за бревнышко, плывешь вниз по течению. вскоре тебя спасают рыбаки, и ты узнаешь, что случилось с твоими замками и семьей."
        bot.send_photo(message.chat.id, WarriorStory.castle_001())
        text_warrior_01 = "Продолжить"
        text_warrior_02 = "Желая вернуть утраченное, ты решаешь отправиться в столицу, чтобы просить помощи у императора. Но куда приведет тебя это путешествие?"
        keyboard = types.ReplyKeyboardMarkup(
            row_width=1, resize_keyboard=True)

        bt_warrior_1 = types.KeyboardButton(text=text_warrior_01)
        user_states.pop(message.chat.id)
        user_states[message.chat.id] = 'continue_state_2'
        keyboard.add(bt_warrior_1)
        bot.send_message(message.chat.id, text_warrior,
                         parse_mode='html')
        bot.send_message(message.chat.id, text_warrior_02,
                         reply_markup=keyboard, parse_mode='html')

    elif user_states.get(message.chat.id) == 'continue_state_2' and message.text == "Продолжить":
        text_warrior_return = "На пути в столицу ты сталкиваешься с загадочным чародеем. Он предлагает помочь тебе в обмен на выполнение одной маленькой услуги."
        text_warrior_return_01 = "Отправиться в путь"
        bot.send_photo(message.chat.id, WarriorStory.old_man_003())

        user_states.pop(message.chat.id)
        user_states[message.chat.id] = 'return_journey_state'

        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bt_warrior_1 = types.KeyboardButton(text=text_warrior_return_01)
        keyboard.add(bt_warrior_1)
        bot.send_message(message.chat.id, text_warrior_return, reply_markup=keyboard,
                         parse_mode='html')

    elif user_states.get(message.chat.id) == 'return_journey_state' and message.text == "Отправиться в путь":
        text_warrior_return = "На данный момент бот находится в стадии разработки, и ты побывал на Альфа тестировании, Спасибо тебе за твой личний опыт взаимодейставия с ним. По вопросам сотрудничества выможете сомной связаться через \nemal: d.klochkov9421@gmail.com"
        bot.send_photo(message.chat.id, MainGraphic.final_photo())
        bot.send_message(message.chat.id, text_warrior_return,
                         parse_mode='html')

        user_states.pop(message.chat.id)

        keyboard = types.ReplyKeyboardMarkup(
            row_width=0, resize_keyboard=False)


if __name__ == '__main__':
    try:
        # Запуск бота
        bot.polling(none_stop=True)
        # bot.infinity_polling()  # Вы можете использовать одну из этих строк, но не обе
    except Exception as e:
        print(f'Ошибка запуска бота: {e}')
