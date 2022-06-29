from telebot import types, TeleBot

from get_data import ag_testy, vaccinations
from config import token

bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):

    # Keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    positives_negatives = types.KeyboardButton('Positives/Negatives')
    vaccinations_ = types.KeyboardButton('Vaccinations')
    markup.add(positives_negatives, vaccinations_)

    # Message
    bot.send_message(
        message.chat.id, 'This bot gives information about the number of positive-negative '
                         'tests, the number of vaccinated people in the Slovak Republic \n\n'
                         'Click the button below to get started',
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def callback(message):
    if message.chat.type == 'private':
        if message.text == 'Positives/Negatives':
            bot.send_message(
                message.chat.id,
                f'Total positives: {ag_testy()["positives_count"]}\n'
                f'Total negatives: {ag_testy()["negatives_count"]}\n\n'
                f'Date: {ag_testy()["updated_at"]}'
            )
        if message.text == 'Vaccinations':
            bot.send_message(
                message.chat.id,
                f'Total dose 1: {vaccinations()["dose1_sum"]}\n'
                f'Total dose 2: {vaccinations()["dose2_sum"]}\n\n'
                f'Date: {vaccinations()["updated_at"]}'
            )


bot.polling()
