import telebot
from config import TOKEN
from keyboard import keyboardStart, keyboardTimezone

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите язык/Choose language', reply_markup=keyboardStart)


@bot.message_handler(commands=['timezone'])
def define_timezone(message):
    print(message.location)
    bot.send_message(message.chat.id,
                     'Нажмите на кнопку для определения вашего часового пояса', reply_markup=keyboardTimezone)
    a = message.location


bot.polling(none_stop=True)