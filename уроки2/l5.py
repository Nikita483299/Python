# 7444052645:AAGM_GUabJtxI9k7_rDtk7b99eCJgTBiAPU
import telebot
from telebot import types
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup as Bs

token = '7444052645:AAGM_GUabJtxI9k7_rDtk7b99eCJgTBiAPU'
bot = telebot.TeleBot(token=token)

lst_bot = ["paper.png", "stone.png", "scissors.png", 
           "stone.png", "scissors.png", "paper.png", 
           "scissors.png", "paper.png", "stone.png"]

dct_result = {
    "user": 0,
    "bot": 0,
    "draw": 0
}

@bot.message_handler(commands=['start'])
def main_func(message):
    user = bot.send_message(
        message.chat.id,
       text="бот запущен",
       reply_markup=keyboard()
    )
    bot.register_next_step_handler(user, option_func)

def option_func(message):
    if message.text == "reminders":
        set_reminder(message)

    elif message.text == "Game":
        game_func(message)

def game_func(message):
    buttons = types.ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True
    )
    button1 = types.KeyboardButton(text="Paper")
    button2 = types.KeyboardButton(text="Stone")
    button3 = types.KeyboardButton(text="Scissors")
    button4 = types.KeyboardButton(text="Exit")
    buttons.add(button1, button2, button3, button4)

    user_choice = bot.send_message(
        message.chat.id,
        text="Выберай:",
        reply_markup=buttons
    )
    bot.register_next_step_handler(user_choice, game_options)

def game_options(message):
    bot_choice = random.choice(lst_bot)
    try:
        bot.send_sticker(message.chat.id, open(f"images/{message.text.lower()}.png", "rb"))
        bot.send_sticker(message.chat.id, open(f"images/{bot_choice}", "rb"))
    except FileNotFoundError:
        bot.reply_to(message, text="Ошибка.")


@bot.message_handler(commands=["setreminder"]) # регистрация команды /setreminder
def set_reminder(message):
    bot.reply_to( # ответ на команду
        message, # переменная в которую записуеться значение ответа
        text='enter datetime in format: YYYY-MM-DD HH:MM' # сам ответ на команду
    )

    bot.register_next_step_handler(message, handle_message) # тормоз кода до написания ответа на сообщение бота

def handle_message(message):
    try:
        reminder_datetime = datetime.strptime(message.text, "%Y-%m-%d %H:%M") # сравнивание типа
        if reminder_datetime < datetime.now():
            bot.reply_to(message, text="купи себе календарь")
        else:
            bot.send_message(
                message.chat.id,
                text=f"reminder set to: {reminder_datetime}")

            send_reminder(message, reminder_datetime)
    except ValueError:
        bot.reply_to(message,
                     text="invalid datetime format"
                     )

def send_reminder(message, reminder_datetime):
    while True:
        if datetime.now() >= reminder_datetime:
            bot.reply_to(message, text=f"TIME! {reminder_datetime}")
            break

def keyboard(): # функция добавления кнопок
    buttons = types.ReplyKeyboardMarkup( # настройки кнопок
        resize_keyboard=True,
        row_width=2
    )

    button1 = types.KeyboardButton(text="reminders") # кнопка 1 с названием Reminders
    button2 = types.KeyboardButton(text="Game") # кнопка 2
    button3 = types.KeyboardButton(text="button3") # кнопка 3
    buttons.add(button1, button2, button3) # общая переменная которая связует кнопки с настройками и используеться для вызова кнопок

    return buttons # вернуть buttons (переменную выше)


if __name__ == '__main__':
    bot.polling(non_stop=True)