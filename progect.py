import telebot


bot = telebot.TeleBot('6612755394:AAGAE7cSWS5gCAaF0y7N48eUnxJSv957HhY')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Пожалуйста, Введите выражение для вычисления.')

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, str(result))
    except:
        bot.reply_to(message, 'Извините, мы не можем решить данный пример.')


bot.polling()