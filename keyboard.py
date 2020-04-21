from telebot import types


keyboardStart = types.InlineKeyboardMarkup(row_width=2)
keyRU = types.InlineKeyboardButton(text='Русский', callback_data='Ru')
keyEng = types.InlineKeyboardButton(text='English', callback_data='Eng')
keyboardStart.add(keyRU, keyEng)

keyboardTimezone = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttonKtz = types.KeyboardButton('Отправить свою локацию', request_location=True)
keyboardTimezone.add(buttonKtz)
