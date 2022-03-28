import os
import telebot
import level
import importlib

from rjson import Rjson
import cat

TOKEN = os.environ.get('API_TOKEN')
yo = '779130626'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
bot.messages = Rjson('bd/messages.json')
bot.triggers = Rjson('bd/triggers.json')
bot.users = Rjson('bd/users.json')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands = ['ranking'])
def send_ranking(message):
    importlib.reload(level)
    ranking = level.get_rank(bot)
    bot.reply_to(message, ranking)

@bot.message_handler(commands = ['cat', 'cats', 'gato', 'gata'])
def send_cat(message):
    CATAAS = "https://cataas.com/cat"
    if len(message.text)>3:
        CATAAS = f"https://cataas.com/cat/says/{message.text.split(' ', 2)[1]}"
    r = cat.download_image(CATAAS)
    with open('cat.png','rb') as r2:    
        bot.send_photo(message.chat.id, r2)

    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    importlib.reload(level)
    #print(level.VERSION)
    print(message)
    level.save_metadata(message, bot)
    level.update_xp(message, bot)
    autoreply = level.get_autoreply(message, bot)
    print(autoreply)
    if autoreply != "":
        bot.reply_to(message, autoreply)


bot.infinity_polling()
