import telebot

# создаем словарь со словами и их переводами
word_dict = {
    "цветок": "цецг",
    "чаша": "ааһ",
    "четыре": "дөрвн",
    "дерево": "модн",
    "зелёный": "ноһан",
    "кошка": "мис",
    "камень": "чолун",
    "красный": "улан",
    "лиса": "арат",
    "мышь": "хулһн",
    "собака": "ноха",
    "знамя": "туг",
    "транспорт": "көлгн",
    "рука": "һар",
    "дом": "гер",
    "птица": "шовун",
    "табун": "адун"    
    #  слова и их переводы
}


bot = telebot.TeleBot("Tокен бота")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-словарь. Просто напиши мне калмыцком языке, и я выдам тебе его перевод на русский..")

@bot.message_handler(func=lambda message: True)
def send_translation(message):
    word = message.text.lower()
    translation = word_dict.get(word)
    if translation:
        bot.reply_to(message, f"Перевод слова '{word}' - '{translation}'")
    else:
        bot.reply_to(message, "Извините, перевод для данного слова не найден.")

# запускаем бота
bot.polling()