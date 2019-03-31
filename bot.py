import config
import telebot
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def mirrormessage(message):
    if message.text == 'Леонид Овчинников':
        bot.send_message(message.chat.id, 'Тут должна быть ваша пасхалка ')
    else:
        bot.send_message(message.chat.id, message.text)
if __name__ =='__main__':
    bot.polling(none_stop=True)