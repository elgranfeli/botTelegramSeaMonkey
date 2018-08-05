#modulos
import telebot,datetime

bot = telebot.TeleBot("505419661:AAFqNd_5umKWcl30shM9q8ua-oXJgQjHcys")

@bot.message_handler(commands=['start'])
def saludo(message):
	print "DONE START"
	bot.send_message(message.chat.id, "Welcome to my world, I will help you about likes, comments, etc on instagram")

@bot.message_handler(commands=['help'])
def saludo(message):
	print "DONE HELP"
	bot.send_message(message.chat.id, "If you want to check another commands press  @SeaMonkeyBot")

@bot.message_handler(commands=['info'])
def saludo(message):
        print "DONE COMMAND1"
        bot.send_message(message.chat.id, "Visit my profile and make sure doing well http://instagram.com/felicecucolo")

#hora
@bot.message_handler(commands=['time'])
def send_time(message):
    bot.send_message(message.chat.id, "Current time:" + str(datetime.datetime.now()))

bot.polling()
