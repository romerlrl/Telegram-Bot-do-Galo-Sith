from random import randint
from rjson import Rjson

import re

import triggers

def update_xp(message, bot):
    users = bot.users
    userid = str(message.from_user.id)

    if users.data.get(userid, None) is None:
        users.data[userid] = {
            'username':message.from_user.first_name,
            'xp':randint(1, 10)
        }
    else:
        users.data[userid]['username'] = message.from_user.first_name
        users.data[userid]['xp']+=randint(1, 10)
        
    users.commit()

def save_metadata(message, bot):
    messages = bot.messages
    messages.data[message.id] = {
            'author' : message.from_user.id,
            'datetime' : message.date,
            'chat' : message.chat.id,
            'len': len(message.text)
        }
    messages.commit()

def get_rank(bot):
    users = Rjson('bd/users.json')
    ranking = [( val.get('xp'), val.get('username')) for  val in users.data.values()]
    ranking.sort(reverse=1)
    size = len(str(ranking[0][0]))
    rank = 'Ranking do server'
    for xp, name in ranking:
        rank+=f'\n{str(xp).rjust(size+2, "0")}  :  {name}'
    
    return rank
    
def get_autoreply(message, bot):
    tr = bot.triggers
    for trigger, response in tr.data.items():
        if re.search(trigger, message.text.lower()):
            fun = triggers.identity
            if response.startswith('function'):
                fun = triggers.functions[response]
            return fun(message.text, response, message.from_user.first_name)
    return ''                
    
    
VERSION = 6