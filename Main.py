import telebot
from telebot import types

token = "6827408238:AAGGauvH6NG8aGqvaNDODiizvOiwfp2TbzQ"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    item2 = types.KeyboardButton("Кнопка 2")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def message_reply(message):
#     if message.text == "Кнопка":
#         bot.send_message(message.chat.id, "https://habr.com/ru/users/lubaznatel/")


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Кнопка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Кнопка 2")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
    elif message.text == "Кнопка 2":
        bot.send_message(message.chat.id, 'Спасибо за прочтение статьи!')


bot.infinity_polling()


