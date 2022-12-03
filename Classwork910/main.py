import telebot
import time
#
bot = telebot.TeleBot('Здесь твой токен, полученный от @botfather')
#
CHANNEL_NAME = 'Bebra'
#
f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
#
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    #
    time.sleep(30)
bot.send_message(CHANNEL_NAME, "Жарти закінчилися :(")