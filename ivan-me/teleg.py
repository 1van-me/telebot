import telebot

import requests

bot = telebot.TeleBot('750884164:AAFu64eynHgdu4AtM3SssgT54JoPZmZx0xY')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('спокойной ночи', 'доброе утро', 'включи музыку', 'погода')

def weather(message):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = message.text
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']['temp']
    format_add = round(format_add -273.15)
    weather = json_data["weather"], [0], ["main"]
    bot.send_message(message.chat.id,'В городе ' + message.text + ' ' + str(format_add)+'°C', weather)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text.lower() == 'бум':
        exit()
    
    elif message.text.lower() == 'привет':
        bot.send_message (message.chat.id, 'Приветствую')

    elif message.text.lower() =='для чего тебя создали?':
        bot.send_message (message.chat.id, 'Я создан замечательным человеком, в качестве личного помощника ')
    
    elif message.text.lower() =='кто твой создатель?':
        bot.send_message (message.chat.id, 'Замечательный человек: https://vk.com/1van_me ')

    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'Замечательно, а у вас?')
    elif message.text.lower() == 'хорошо':
        bot.send_message (message.chat.id, 'Мне радостно за вас')
    elif message.text.lower() == 'плохо':
        bot.send_message (message.chat.id, 'Жаль')

    elif message.text.lower() == 'доброе утро':
        bot.send_sticker(message.chat.id, 'CAADAgAD4AgAAgi3GQKT5DnrvOwaLAI')
        audio = open('Queen - I wan to break free.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)

    elif message.text.lower() == 'спокойной ночи':
        bot.send_message(message.chat.id, "https://www.youtube.com/?hl=ru" )

    elif message.text.lower() == 'отправь стикер':
        bot.send_sticker(message.chat.id, 'CAADAgADrAgAAgi3GQKUnP3BgI8D6gI')

    elif message.text.lower() == 'что делаешь?':
        bot.send_message (message.chat.id, 'Функционирую')


    elif message.text.lower() == 'включи музыку':
        bot.send_message(message.chat.id, 'какую?')
    elif message.text.lower() == 'квин':
        audio = open('Queen - I wan to break free.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio = open('Queen - Bohemian rhapsody.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio = open('Queen - we are the champions.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio = open('Queen - We will rock you.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text.lower() == 'битлс':
        audio = open('The beatles - and i live her.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio = open('The beatles - come together.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio = open('The beatles - yellow submarine.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text.lower() == 'грустную':
        audio = open('123.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio = open('Young Pinch - Leave me alone.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio = open('Tom Walker - Leave a Light on.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    

    
        
    elif message.text.lower() == 'погода':
        msg=bot.send_message(message.chat.id,"Введите город (На английском, с большой буквы)")
        bot.register_next_step_handler(msg, weather)

    elif message.text.lower() =='кто тебя создал?':
        bot.send_message (message.chat.id, 'Замечательный человек: https://vk.com/1van_me ')

    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю')

        

        #if weather == 'Snow':
         #   photo = open('snow.jpg', 'rb')
        #    bot.send_photo(message.chat.id, photo)
        #elif weather == 'Clear':
         #   photo = open('clear.jpg', 'rb')
        #    bot.send_photo(message.chat.id, photo)           
       # elif weather == 'Clouds':
         #   photo = open('Сlouds.jpg', 'rb')
        #    bot.send_photo(message.chat.id, photo)             
       # elif weather == 'Mist':
          # photo = open('mist.jpg', 'rb')
         #  bot.send_photo(message.chat.id, photo)                          
        #elif weather == 'Dark':
       #    photo = open('dark.png', 'rb')
      #      bot.send_photo(message.chat.id, photo)

        

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
bot.polling()