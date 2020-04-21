import telebot

import types


keyboardStart = types.InlineKeyboardMarkup(row_width=2)
keyRU = types.InlineKeyboardButton(text='Русский', callback_data='Ru')
keyEng = types.InlineKeyboardButton(text='English', callback_data='Eng')
keyboardStart.add(keyRU, keyEng)

keyboardTimezone = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttonKtz = types.KeyboardButton('Отправить свою локацию', request_location=True)
keyboardTimezone.add(buttonKtz)


#
from config import TOKEN
#from keyboard import keyboardStart, keyboardTimezone

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