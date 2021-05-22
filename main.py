#  Copyright (c) ChernV (@otter18), 2021.

import os
import random

from setup import bot, logger
from webhook import app

# --------------- dialog params -------------------
dialog = {
    'hello': {
        'in': ['hello', 'hi', 'privet', 'hey','Hello', 'Hi','Hey'],
        'out': ['What`s up', 'Yo Nigga', 'Sup bro!', 'Hey! Me so horny!', 'GET OVER HERE!']
    },
    'привет': {
        'in': ['привет', 'Здравствуйте', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    'how r u': {
        'in': ['как дела', 'как ты', 'how are you', 'дела', 'how is it going'],
        'out': ['Хорошо', 'Отлично', 'Good. And how are u?']
    },
    'name': {
        'in': ['зовут', 'name', 'имя'],
        'out': [
            'Я telegram-template-bot',
            'Я бот шаблон, но ты можешь звать меня в свой проект',
            'Это секрет. Используй команду /help, чтобы узнать'
        ]
    }
}


# --------------- bot -------------------
@bot.message_handler(commands=['start'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        '<b>Hello! Wellcome to Bullion.Media <a href="https://bullion.media/">Bullion.Media</a></b>',
        parse_mode='html'
    )
    
    
@bot.message_handler(commands=['publisher'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        '<b>Hello! Get your publishers stats  <a href="https://admin.bullionyield.com/publisher/login">Bullion.Yield</a></b>',
        parse_mode='html'
    )
    
    
@bot.message_handler(commands=['advertiser'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        '<b>Hello! Get your publishers stats  <a href="https://admin.bullionyield.com/advertiser/login">Bullion.Yield</a></b>',
        parse_mode='html'
    )
    

@bot.message_handler(commands=['admin'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        '<b>Let`s ROCK them today!  <a href="https://admin.bullionyield.com/admin/login">Bullion.Yield</a></b>',
        parse_mode='html'
    )
    
    bot.infinity_polling()
