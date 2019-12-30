#! python3
# -*- coding: utf-8 -*-

import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

with open('bot_info.json', 'r') as f:                                 # Get Connection Info
    connection_data = json.load(f)

updater = Updater(token=connection_data["token"], use_context=True)   # Create Updater
dispatcher = updater.dispatcher                                       # Create Dispatcher


### Basic Functions ###

def start(update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hi {}!".format(user.first_name))


def display_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Comandi disponibili:\n -- ")


# To handle wrong commands
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Command Unknown!")


# Example:
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# <-- TODO: Add new functionality


### HANDLERS ###

# Create Handlers
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', display_help)
echo_handler = MessageHandler(Filters.text, echo)
# <-- TODO: Create new handler

# Add handlers to Dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(echo_handler)
# <-- TODO: Add new handler to dispatcher


### Unknown Commands Handler - Must be the last handler added to dispatcher! ###
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

### START BOT ###
updater.start_polling()
print("Bot Started!")
