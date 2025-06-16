# 7444052645:AAGM_GUabJtxI9k7_rDtk7b99eCJgTBiAPU
# библиотеки
import telebot
from telebot import types
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup as Bs

token = '7519476534:AAFtRjZAtmgxzdCIX_KDc8bbzIWQokvBFAU' # token учителя
bot = telebot.TeleBot(token=token) # создание переменной отвечающей за токеном

@bot.message_handler(commands=['start']) # регистрация команды старт
def main_func(message): # функция команды старт
    bot.send_message( # вывести сообщение
        message.chat.id, # получение айди пользователя (кому отвечать и на что)
        text="помилка." # сам ответ
    )

if __name__ == '__main__': # хз что это
    bot.polling(non_stop=True) # хз что это