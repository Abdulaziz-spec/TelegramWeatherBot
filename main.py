import wikipedia
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove
from buttons import menu_buttons
from func_bot import country_info, weather_info

wikipedia.set_lang('ru')

TOKEN = 'your-token'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    username = message.from_user.username
    bot.send_message(chat_id, f'''Здраствуйте {username} вас приветсвует информационый БОТ
Выберете то что вас интрересует нажав на кнопку''', reply_markup=menu_buttons())


@bot.message_handler(regexp='Википедия📚')
def reaction_wikipedia(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    bot.send_message(chat_id, 'Введите Текст Для Поиска В Википедии', reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_text_wikipedia)


def get_text_wikipedia(message: Message):
    chat_id = message.chat.id
    text = message.text
    try:
        result = wikipedia.summary(text)
    except:
        result = 'По вашему вопросу нечего не найдено'
    bot.send_message(chat_id, result, reply_markup=menu_buttons())


# =========================================================================================================

@bot.message_handler(regexp='Страны🌐')
def reaction_country(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    bot.send_message(chat_id, 'Введите Название Страны Для Получение Информации', reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_text_country)


def get_text_country(message: Message):
    chat_id = message.chat.id
    country = message.text
    try:
        result = country_info(country)
    except:
        result = 'По вашему Запросу нечего не найдено'
    bot.send_message(chat_id, result, reply_markup=menu_buttons())


# ==============================================================================================================

@bot.message_handler(regexp='Погода☀')
def reaction_weather(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Введите название города для получения информации о погоде:',
                     reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_text_weather)


def get_text_weather(message: Message):
    chat_id = message.chat.id
    city = message.text
    try:
        result = weather_info(city)
    except:
        result = 'Простите я не нашел Информацию по вашему запросу'
    bot.send_message(chat_id, result, reply_markup=menu_buttons())


bot.polling(none_stop=True)
