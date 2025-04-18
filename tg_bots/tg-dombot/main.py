import json
import requests
import telebot
from telebot import types

url = 'https://crm.atformula.ru/api/telegram/dombot/webhook/cad3fe936a310572ad36b2b03ba538e1'
headers = {
    "Content-type": "application/json"
}

d = dict()
x = dict.fromkeys(["request", "type", "name", "code", "phone", "id", "firstname-tg", "lastname-tg", "username-tg", "exists"])
bot = telebot.TeleBot("6427859700:AAHCe_SA0XbocsEfTWX_-ma4bYGhCTnorAM")


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@bot.message_handler(commands=['start'])
def start(message):
    x["request"] = ""
    x["type"] = ""
    x["name"] = ""
    x["code"] = ""
    x["phone"] = ""
    x["firstname-tg"] = message.from_user.first_name
    x["lastname-tg"] = message.from_user.last_name
    x["username-tg"] = message.from_user.username


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("\U0001F4CD Согласование перепланировки")
    btn2 = types.KeyboardButton("\U0001F4CD Приемка кваритры от застройщика")
    markup.add(btn1).add(btn2)
    bot.send_message(message.from_user.id, "По какому вопросу Вы обращаетесь?", reply_markup=markup)

    


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id,
                     "Для старта напишите /start. \n\nЕсли у вас остались вопросы, свяжитесь с нами по номеру телефона +7 913 970-00-37",
                     reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '\U0001F4CD Согласование перепланировки':
        x["request"] = 'Согласование перепланировки'
        url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
        r = requests.get(url1)
        r = r.json()
        flag = r["exists"]
        if not flag:
            bot.send_message(message.from_user.id, 'Напишите Ваше имя и фамилию',
                            reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_name)
        else:
            bot.send_message(message.from_user.id, "Вы уже зарегестрированы в боте\n\nВведите кодовое слово. Если кодовое слово Вам неизвестно, напишите 'Другое'",  reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_code)



    elif message.text == '\U0001F4CD Приемка кваритры от застройщика':
        x["request"] = 'Приемка кваритры от застройщика'
        url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
        r = requests.get(url1)
        r = r.json()
        flag = r["exists"]
        if not flag:
            bot.send_message(message.from_user.id, 'Напишите Ваше имя и фамилию',
                            reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_name1)
        else:
            bot.send_message(message.from_user.id,
                     "Вы уже зарегестрированы в боте\n\nВведите кодовое слово. Если кодовое слово Вам неизвестно, напишите 'Другое'",  reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_code1)

    elif message.text == '\U0001F4CD Планируемая (ремонт еще не выполнен)':
        x["type"] = 'Планируемая (ремонт еще не выполнен)'
        url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
        r = requests.get(url1)
        r = r.json()
        flag = r["exists"]
        if not flag:
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            reg_button = types.KeyboardButton(text="Поделиться номером", request_contact=True)
            keyboard.add(reg_button)
            bot.send_message(message.from_user.id, 'Укажите Ваш номер телефона для связи. Для этого нажмите на кнопку ниже \U00002B07',
                            reply_markup=keyboard)
            bot.register_next_step_handler(message, get_phone0)
        else:
            x["id"] = message.from_user.id
            x["exists"] = True
            bot.send_message(message.from_user.id,
                     'Мы обязательно свяжемся с Вами для выяснения деталей.\n\n\U0001F31F Бонус! \U0001F31F \nМы '
                     'выплачиваем комиссию за каждую рекомендацию',
                     reply_markup=types.ReplyKeyboardRemove())
            ans = json.dumps(x, ensure_ascii=False).encode('utf-8')
            requests.post(url, headers=headers, data=ans)
        

    elif message.text == '\U0001F4CD Выполненная (ремонт уже выполнен)':
        x["type"] = 'Выполненная (ремонт уже выполнен)'
        url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
        r = requests.get(url1)
        r = r.json()
        flag = r["exists"]
        if not flag:
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            reg_button = types.KeyboardButton(text="Поделиться номером", request_contact=True)
            keyboard.add(reg_button)
            bot.send_message(message.from_user.id, 'Укажите Ваш номер телефона для связи. Для этого нажмите на кнопку ниже \U00002B07',
                            reply_markup=keyboard)
            
            bot.register_next_step_handler(message, get_phone)
        else:
            x["id"] = message.from_user.id
            x["exists"] = True
            bot.send_message(message.from_user.id,
                     'Мы обязательно свяжемся с Вами для выяснения деталей.\n\n\U0001F31F Бонус! \U0001F31F \nМы '
                     'выплачиваем комиссию за каждую рекомендацию',
                     reply_markup=types.ReplyKeyboardRemove())
            ans = json.dumps(x, ensure_ascii=False).encode('utf-8')
            requests.post(url, headers=headers, data=ans)
        

    elif message.text == '\U0001F4CD Стоимость квартиры более 20 млн':
        x["type"] = 'Стоимость квартиры до 20 млн'
        url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
        r = requests.get(url1)
        r = r.json()
        flag = r["exists"]
        if not flag:
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            reg_button = types.KeyboardButton(text="Поделиться номером", request_contact=True)
            keyboard.add(reg_button)
            bot.send_message(message.from_user.id, 'Укажите Ваш номер телефона для связи. Для этого нажмите на кнопку ниже \U00002B07',
                            reply_markup=keyboard)
            bot.register_next_step_handler(message, get_phone2)
        else:
            x["id"] = message.from_user.id
            x["exists"] = True
            bot.send_message(message.from_user.id,
                     '\U0001F525 Эксклюзивные условия для партнеров по приемке квартир от застройщика!',
                     reply_markup=types.ReplyKeyboardRemove())
            ans = json.dumps(x, ensure_ascii=False).encode('utf-8')
            requests.post(url, headers=headers, data=ans)

        

    elif message.text == '\U0001F4CD Стоимость квартиры до 20 млн':
        x["type"] = 'Стоимость квартиры до 20 млн'
        url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
        r = requests.get(url1)
        r = r.json()
        flag = r["exists"]
        if not flag:
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            reg_button = types.KeyboardButton(text="Поделиться номером", request_contact=True)
            keyboard.add(reg_button)
            bot.send_message(message.from_user.id, 'Укажите Ваш номер телефона для связи. Для этого нажмите на кнопку ниже \U00002B07',
                            reply_markup=keyboard)
            bot.register_next_step_handler(message, get_phone3)
        else:
            x["id"] = message.from_user.id
            x["exists"] = True
            bot.send_message(message.from_user.id,
                     '\U0001F525 Эксклюзивные условия для партнеров по приемке квартир от застройщика!',
                     reply_markup=types.ReplyKeyboardRemove())
            ans = json.dumps(x, ensure_ascii=False).encode('utf-8')
            requests.post(url, headers=headers, data=ans)
        

    else:
        bot.send_message(message.from_user.id, "Для старта напишите /start.", reply_markup=types.ReplyKeyboardRemove())


def get_name(message):
    x["name"] = message.text
    bot.reply_to(message, "Приятно познакомиться, " + message.text + "!\n\nВведите кодовое слово. Если кодовое слово Вам неизвестно, напишите 'Другое'")
    bot.register_next_step_handler(message, get_code)


def get_name1(message):
    x["name"] = message.text
    bot.reply_to(message, "Приятно познакомиться, " + message.text + "!\n\nВведите кодовое слово. Если кодовое слово Вам неизвестно, напишите 'Другое'")
    bot.register_next_step_handler(message, get_code1)


def get_phone0(message):
    x["phone"] = message.contact.phone_number
    x["id"] = message.from_user.id
    url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
    r = requests.get(url1)
    r = r.json()
    flag = r["exists"]
    if not flag:
        x["exists"] = False
    ans = json.dumps(x, ensure_ascii=False).encode('utf-8')
    requests.post(url, headers=headers, data=ans)

    bot.send_message(message.from_user.id,
                     'Мы обязательно свяжемся с Вами для выяснения деталей.\n\n\U0001F31F Бонус! \U0001F31F \nМы '
                     'выплачиваем комиссию за каждую рекомендацию',
                     reply_markup=types.ReplyKeyboardRemove())


def get_phone(message):
    x["phone"] = message.contact.phone_number
    x["id"] = message.from_user.id
    url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
    r = requests.get(url1)
    r = r.json()
    flag = r["exists"]
    if not flag:
        x["exists"] = False
    ans = json.dumps(x, ensure_ascii=False).encode('utf-8')
    requests.post(url, headers=headers, data=ans)
    bot.send_message(message.from_user.id,
                     'Мы обязательно свяжемся с Вами для выяснения деталей.\n\n\U0001F31F Бонус! \U0001F31F \nМы '
                     'выплачиваем комиссию за каждую рекомендацию',
                     reply_markup=types.ReplyKeyboardRemove())


def get_phone2(message):
    x["phone"] = message.contact.phone_number
    x["id"] = message.from_user.id
    url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
    r = requests.get(url1)
    r = r.json()
    flag = r["exists"]
    if not flag:
        x["exists"] = False
    ans = json.dumps(x, ensure_ascii=False).encode('utf-8')
    requests.post(url, headers=headers, data=ans)
    bot.send_message(message.from_user.id,
                     '\U0001F525 Эксклюзивные условия для партнеров по приемке квартир от застройщика!',
                     reply_markup=types.ReplyKeyboardRemove())


def get_phone3(message):
    x["phone"] = message.contact.phone_number
    x["id"] = message.from_user.id
    url1 = 'https://crm.atformula.ru/api/telegram/dombot/userexists/cad3fe936a310572ad36b2b03ba538e1/' + str(message.from_user.id) 
    r = requests.get(url1)
    r = r.json()
    flag = r["exists"]
    if not flag:
        x["exists"] = False
    ans = json.dumps(x, ensure_ascii=False).encode('utf-8')
    requests.post(url, headers=headers, data=ans)
    bot.send_message(message.from_user.id,
                     '\U0001F525 Эксклюзивные условия для партнеров по приемке квартир от застройщика!',
                     reply_markup=types.ReplyKeyboardRemove())


def get_code(message):
    x["code"] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("\U0001F4CD Планируемая (ремонт еще не выполнен)")
    btn2 = types.KeyboardButton("\U0001F4CD Выполненная (ремонт уже выполнен)")
    markup.add(btn1).add(btn2)
    bot.reply_to(message, "Согласование какой квартиры Вас интересует?", reply_markup=markup)


def get_code1(message):
    x["code"] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("\U0001F4CD Стоимость квартиры до 20 млн")
    btn2 = types.KeyboardButton("\U0001F4CD Стоимость квартиры более 20 млн")
    markup.add(btn1).add(btn2)
    bot.reply_to(message, "Приемка какой квартиры Вас интересует?", reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
