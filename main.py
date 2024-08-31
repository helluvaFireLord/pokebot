import telebot 
from config import token
from random import randint
from logic import Pokemon, Wizard, Fighter

bot = telebot.TeleBot(token) 






@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_photo(message.chat.id, pokemon.show_gen_i_red_blue())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")




@bot.message_handler(commands=['atk'])
def atk_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.atk(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, 'Сражаться можно только покемонами')
    else:
        bot.send_message(message.chat.id, 'Чтобы атаковать, нужно ответить на сообщение того, кого хочешь атаковать')
bot.infinity_polling(none_stop=True)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для игры в покемонов, скорее попробуй создать себе покемона, нажимай - /go")

