import telebot
from telebot import types

bot = telebot.TeleBot('7097421145:AAF5XulF9svN4t3TPzpc242EiDvCzZ0e1aU')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    if message.from_user.last_name == None:
     print('')
     bot.send_message(message.chat.id, mess, parse_mode='html')






@bot.message_handler(commands=['website'])
def website (message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Нажать", url ="https://youtu.be/EE-xtCF3T94"))
    bot.send_message(message.chat.id, 'Перейти по ссылке', reply_markup = markup)

@bot.message_handler(commands=['h'])
def help (message):
    markup = types.InlineKeyboardMarkup()
    website = types.InlineKeyboardButton('Веб')
    start = types.InlineKeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейти по ссылке', reply_markup = markup)

@bot.message_handler()
def get_user_text(message):

    if message.text == "Салам":
        bot.send_message(message.chat.id, "Валейкум", parse_mode='html')
    elif message.text == "Мой":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, f"Иди нахуй {message.from_user.first_name}", parse_mode='html')
bot.polling(none_stop=True)