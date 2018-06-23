from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from datetime import datetime
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    # filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    text = 'Приветствую тебя, мой друг ☺️'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def find_planet(bot, update):
    user_text = update.message.text
    # import pdb; pdb.set_trace()
    planet_name = user_text.split(' ')[-1]
    planet_class = getattr(ephem, planet_name, None)
    if not planet_class:
        update.message.reply_text('Введи планету Марс')
        return
    print(planet_class)
    planet = planet_class(datetime.now().today())
    # planet = str(datetime.now().today())
    update.message.reply_text(ephem.constellation(planet)[1])
        

def main():
    mybot = Updater("580867309:AAEajIB5Cfwi1nPWS-7iNPIFodPxIn21BAo", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', find_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()