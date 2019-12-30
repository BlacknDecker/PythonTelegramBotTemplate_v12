# Telegram Bot Template

This repository contains a simple template to create a telegram bot 
with the [Python Telegram Bot Library](https://python-telegram-bot.org/)
after the version 12 update.

##Usage
### Retrieve a new token
Ask the [BotFather](https://telegram.me/BotFather) for a new bot token.
Follow the instructions and get the token that the BotFather 
will provide you. Then copy the *bot_info_TEMPLATE.json* file and
rename it as *bot_info.json* and put the bot token inside it. 

### Start the bot
Just run the script to start the bot. Type "*/help*" to use the *help* 
command, or type anything without the starting "/" to use the *echo* 
functionality.

### Add new functionalities
To add new commands follow this steps:
1. Create a function that performs the functionality that you want to provide.
    This function must contain two parameters, **update** and **context** 
    (see the documentation for further details).
1. Create the handler that will associate the command to the function.
1. Add the handler to the dispatcher.

### Documentation
##### Python Telegram Bot
* [Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki): 
    contains a lot of useful material.
* [Snippets](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets):
    short examples to explain how to do specific stuff.
* [Examples](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Examples):
    some example of bots created using this library.
* [Documentation](https://python-telegram-bot.readthedocs.io/en/stable/): the library doc.

##### Telegram API
* [Telegram API](https://core.telegram.org/bots/api#authorizing-your-bot):
    official API documentation.