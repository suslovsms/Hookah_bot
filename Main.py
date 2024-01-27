import telebot

token = "6827408238:AAGGauvH6NG8aGqvaNDODiizvOiwfp2TbzQ"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")
    bot.infinity_polling()


# start_message("Привет")
