import telebot
from telebot import types

bot = telebot.TeleBot('5831819924:AAE7P5Uj3fSKOafM5imxB_9aUsrubESRglE')



@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Salom, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler()
# def get_user_text(message):
#     if message.text == 'Salom':
#        bot.send_message(message.chat.id, "Sizga ham Salom !", parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('fonovie-oboi-skachat.640x360.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Sani chunmayaman', parse_mode ='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.id, 'Ux zor rasm ekan!')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Saytga kirish', url='http://proweb.uz'))
    bot.send_message(message.chat.id, 'Otvol saytga tez!', reply_markup=markup)


bot.polling(none_stop=True)