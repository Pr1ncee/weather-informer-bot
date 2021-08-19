"""
This bot gives info about weather in a city you want to know
Uses pyown for getting information about weather
Uses telebot as API for Telegram
"""

# TODO Save 'lang_eng' variable out of program call
# TODO Replace 'output_ru' to 'transator(output_en)' (fix russian formatting)
# TODO Switch 'btn_help_(ru/en)' to the appropriate language when changing the languages

from time import sleep

from deep_translator import GoogleTranslator
import pyowm
from pyowm.owm import OWM
from pyowm.commons import exceptions
from pyowm.utils.config import get_default_config
import telebot
from telebot import types

from config import api_key, token
from degrees_converter import degrees_to_cardinal


bot = telebot.TeleBot(token)
owm = OWM(api_key=api_key)
mgr = owm.weather_manager()

lang_eng = True
translator = GoogleTranslator(source='en', target='ru').translate

output_en = 'Description - {1} {0}' \
            'Temperature(°С) - {2} {0}' \
            'Wind(Km/h) - {3} {0}' \
            'Wind direction - {4} {0}' \
            'Humidity(%) - {5} {0}' \
            'Pressure(mmHg) - {6} {0}' \
            'Sunrise(UTC) - {7} {0}' \
            'Sunset(UTC) - {8}'

# When using 'transator(output_en)' under-indented row appears, besides it some words are NOT 'capitalize()'
output_ru = 'Погода - {1} {0}' \
            'Температура(°С) - {2} {0}' \
            'Ветер(км/ч) - {3} {0}' \
            'Направление ветра - {4} {0}' \
            'Влажность(%) - {5} {0}' \
            'Давление(мм.рт.ст.) - {6} {0}' \
            'Восход(UTC) - {7} {0}' \
            'Закат(UTC) - {8}'

# Adding keyboard's buttons
kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_help_en = types.KeyboardButton('Help')
btn_help_ru = types.KeyboardButton('Помощь')
btn_ru = types.KeyboardButton('RU')
btn_en = types.KeyboardButton('EN')
kb.add(btn_ru)
kb.add(btn_en)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Choose your language below:', reply_markup=kb)
    sleep(4)
    if lang_eng:
        kb.add(btn_help_en)  # The appropriate help button added after '/start'
        bot.send_message(message.chat.id, 'Input a city(for more information click on "Help"):', reply_markup=kb)
    else:
        kb.add(btn_help_ru)  # The appropriate help button added after '/start'
        bot.send_message(
            message.chat.id, 'Введите город(для дополнительной информации нажмите "Помощь"):', reply_markup=kb
                        )


@bot.message_handler(content_types=['text'])
# Main function!
def weather(message):
    global lang_eng

    if message.text == 'Help':
        bot.send_message(message.chat.id,
                         "This bot provides you an information about a weather in any city of the world."
                         + "\n" + "Write a name of any city to know weather:", reply_markup=kb)

    elif message.text == 'Помощь':
        bot.send_message(message.chat.id, "Этот бот предоставляет информацию о погоде в любом городе в мире." + "\n"
                         + "Введите название любого города для того, чтобы узнать погоду:", reply_markup=kb)

    elif message.text == 'RU':
        config = get_default_config()
        config['language'] = 'ru'
        lang_eng = False
        bot.send_message(message.chat.id, 'Язык успешно изменен на Русский')

    elif message.text == 'EN':
        config = get_default_config()
        config['language'] = 'en'
        lang_eng = True
        bot.send_message(message.chat.id, 'The language has successfully changed to English')

    else:
        try:
            obs = mgr.weather_at_place(f'{message.text}')

        except exceptions.NotFoundError:
            bot.send_message(message.chat.id, 'Make sure your city name is right')
        except exceptions.UnauthorizedError:
            bot.send_message(message.chat.id, 'Invalid API Key provided')

        else:
            inf = obs.weather

            dt = {"desc": inf.detailed_status.capitalize(),
                  "temp": inf.temperature(unit='celsius')['temp'],
                  "wind": inf.wind()['speed'],
                  "deg": degrees_to_cardinal(inf.wind()['deg']),
                  "hum": inf.humidity,
                  "pres": inf.pressure['press'],
                  "sunrise": inf.sunrise_time('iso')[-14:-6],
                  "sunset": inf.sunset_time('iso')[-14:-6]}  # Only the time will be displayed (e.g. 17:11:23)

            if lang_eng:
                bot.send_message(message.chat.id, output_en.format('\n',
                                                                   str(dt["desc"]),
                                                                   str(dt["temp"]),
                                                                   str(dt["wind"]),
                                                                   str(dt["deg"]),
                                                                   str(dt["hum"]),
                                                                   str(dt["pres"]),
                                                                   str(dt["sunrise"]),
                                                                   str(dt["sunset"])
                                                                   )
                                 )
            else:
                bot.send_message(message.chat.id, output_ru.format('\n',
                                                                   str(dt["desc"]),
                                                                   str(dt["temp"]),
                                                                   str(dt["wind"]),
                                                                   str(translator(dt["deg"])),
                                                                   str(dt["hum"]),
                                                                   str(dt["pres"]),
                                                                   str(dt["sunrise"]),
                                                                   str(dt["sunset"])
                                                                   )
                                 )


bot.polling(timeout=60)
