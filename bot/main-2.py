import json
import requests
import telebot
from telebot import types


d = dict()
x = dict.fromkeys(["phone", "id", "firstname-tg", "lastname-tg", "username-tg"])
bot = telebot.TeleBot("6564874747:AAFpys8V0Jt64JpnANPYnXKplvX1yxl7rKE")


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

@bot.message_handler(commands=['start'])
def start(message):
    
    x["phone"] = 0
    x["firstname-tg"] = message.from_user.first_name
    x["lastname-tg"] = message.from_user.last_name
    x["username-tg"] = message.from_user.username
    bot.send_message(message.from_user.id, "Привет👋!\nДавайте знакомиться!\nМеня зовут Формулка.\n\nА вас как зовут? Напишите имя и фамилию.")
    
    bot.register_next_step_handler(message, get_name)
    

    

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Для старта напишите /start. \n\nЕсли у вас остались вопросы, свяжитесь с нами по номеру телефона +7 913 970-00-37", reply_markup=types.ReplyKeyboardRemove())




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Я дизайнер 🎨':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Создавать грамотные с точки зрения закона проекты")
        btn2 = types.KeyboardButton("Увеличить свой доход в 2 раза повысив квалификацию")
        btn3 = types.KeyboardButton("Получать повышенную комиссию за рекомендацию клиента")
        markup.add(btn1).add(btn2).add(btn3)
       
       
        bot.send_message(message.from_user.id, "Я люблю разбирать планировочные решения и помогать людям сделать законный ремонт🌟.\n\nА что вам интересно?", reply_markup=markup)
        
    elif message.text == 'Создавать грамотные с точки зрения закона проекты':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)        
        bot.send_message(message.from_user.id, "Здорово🔥!\n\nЯ тоже люблю разбираться в нормах законодательства! \n\nДело в том, что дизайн проекты с законной планировкой не только принесут больше денег, но и помогут вам избежать проблем с законом\n\nВот мои рекомендации👇:\n- пройдите обучающий курс «Коротко о главном в перепланировках» за 19.900 руб. (есть рассрочка) и создавай не только стильные, но и законные интерьеры. \nПодробнее по <a href='http://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
        
    elif message.text == 'Увеличить свой доход в 2 раза повысив квалификацию':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Отлично🔥!\n\nВы можете стать экспертом и открыть для себя новую нишу с высоким чеком!\n\nВот мои рекомендации👇:\n- пройдите обучающий курс «Навык» за 119.900 руб. или «Профессия» за 149.900 руб. (есть рассрочка) и получайте 100 тыс.… 200 тыс.... 300 тыс.… ∞ руб. в месяц на согласованиях, работая с нами в команде.\n 🌟Лучшие студенты смогут пройти стажировку в нашей команде и получать стабильный поток клиентов от компании!!🌟 \nПодробнее по <a href='http://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
        
    elif message.text == 'Получать повышенную комиссию за рекомендацию клиента':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Как часто говорит Анна, «деньги к нам приходят через людей»!\nЕсли нет желания и время осваивать профессию эксперта по перепланировкам, выбирайте партнерство🔥!\n\nВот мои рекомендации👇:\n- предложите клиенту согласовать перепланировку, и получите комиссионное вознаграждение в 10% от суммы договора с клиентом\n- кстати, если вы прошли наш обучающий курс «Формула перепланировок», ваша комиссия удваивается и будет равна 20% от суммы договора с клиентом. \nПодробнее по <a href='http://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
        
    elif message.text == 'Я риэлтор 📑':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Узнать как распознать квартиру с подвохом и не дать себя обмануть во время сделки")
        btn2 = types.KeyboardButton("Стабильность дохода - меньше работать и больше зарабатывать")
        btn3 = types.KeyboardButton("Получать повышенную комиссию за рекомендацию клиента")
        markup.add(btn1).add(btn2).add(btn3)
        bot.send_message(message.from_user.id, "Я люблю работать с недвижимостью.\n\nА что вам интересно?", reply_markup=markup)
        
    elif message.text == 'Узнать как распознать квартиру с подвохом и не дать себя обмануть во время сделки':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Здорово🔥!\n\nЯ тоже не хочу иметь проблемы с законом!\n\nВот мои рекомендации👇:\n- пройдите обучающий курс «Коротко о главном в перепланировках» за 19.900 руб. (есть рассрочка), чтобы видеть перепланировки на объектах недвижимости, понимать величину торга, быть авторитетом в глазах клиента. \nПодробнее по <a href='http://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
        
    elif message.text == 'Стабильность дохода - меньше работать и больше зарабатывать':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Отлично🔥!\n\nВы наконец сможете получать высокий, а главное стабильный заработок, ведь не каждый показ заканчивается продажей, но многие могут закончиться согласованием перепланировки!\n\nВот мои рекомендации👇:\n- пройдите обучающий курс «Навык» за 119.900 руб. или «Профессия» за 149.900 руб. (есть рассрочка) и получайте 100 тыс.… 200 тыс.... 300 тыс.… ∞ руб. в месяц на согласованиях, работая с нами в команде.\n 🌟Лучшие студенты смогут пройти стажировку в нашей команде и получать стабильный поток клиентов от компании!!🌟 \nПодробнее по <a href='http://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)

    elif message.text == 'Я собственник квартиры 🏠':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Нашел перепланировку в своей квартире")
        btn2 = types.KeyboardButton("Понял, как нужно законно сделать ремонт")
        btn3 = types.KeyboardButton("Просто было интересно")
        markup.add(btn1).add(btn2).add(btn3)
        bot.send_message(message.from_user.id, "Я понимаю, квартира - ценный актив 📈 и потерять ее из-за незнания закона о перепланировках не лучшая история. Также, я люблю улучшать свою квартиру, перестраивать ее и делать ремонт. Надеюсь, и вы тоже.\n\nВаши впечатления от курса👇:", reply_markup=markup)
        
    elif message.text == 'Нашел перепланировку в своей квартире':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу согласовать сам")
        btn2 = types.KeyboardButton("Хочу получить услугу «согласование перепланировки")
        markup.add(btn1).add(btn2)
        bot.send_message(message.from_user.id, "Перепланировки - дело обычное! Главное, перепланировку узаконить и привести документы в порядок🌟!", reply_markup=markup) 
    
    elif message.text == 'Хочу согласовать сам':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Согласование перепланировки - “увлекательный процесс”. Но самостоятельное согласование поможет сэкономить.\n\nВот мои рекомендации👇:\n- закажите проектно-техническую документацию и получите пошаговый план согласования. \nПодробнее по <a href='https://formula-ncpr.ru/?ysclid=lnlydy4hjy317154263'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
        
    elif message.text == 'Хочу получить услугу «согласование перепланировки':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Согласование перепланировки - длительный и хлопотный процесс. Передайте эту работу специалистам и освободите время для жизни🌟!\n\nВот мои рекомендации👇:\n- вы оставили свои данные и мы с вами обязательно свяжемся! \nПодробнее по <a href='https://formula-ncpr.ru/?ysclid=lnlydy4hjy317154263'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
        
    elif message.text == 'Просто было интересно':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Отлично🔥, спасибо за обратную связь, если остались вопросы, свяжитесь с нами +7 913 970-00-37.\n\nМы поможем согласовать перепланировку любой сложности.\n\n- если вам интересная сфера перепланировок, пройдите наш обучающий курс.\nПодробнее по <a href='https://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
    
    elif message.text == 'Понял, как нужно законно сделать ремонт':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Отлично🔥, спасибо за обратную связь, если остались вопросы, свяжитесь с нами +7 913 970-00-37.\n\nМы поможем согласовать перепланировку любой сложности.\n\n- если вам интересная сфера перепланировок, пройдите наш обучающий курс.\nПодробнее по <a href='https://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
        
    elif message.text == 'Я инвестор в недвижимость 💵':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Я тоже люблю инвестиции в недвижимость🔥!\n\nНедвижимость - самый ценный актив, и он должен быть защищен🔒.\n\nЧтобы инвестиции в недвижимость приносили прибыль, а не хлопоты, воспользуйтесь рекомендациями👇:\n- получите экспертизу объекта недвижимости на предмет наличия перепланировки, или возможности увеличить стоимость недвижимости за счет согласования или за счет разделения объекта\n\n- если вам интересная сфера перепланировок, пройдите наш обучающий курс. \nПодробнее по <a href='https://formula-ncpr.ru/?ysclid=lnlydy4hjy317154263'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)

        
    elif message.text == 'Я в поисках дохода 🎯':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.send_message(message.from_user.id, "Отлично🔥, я покажу тебе, что ниша перепланировок очень прибыльна.\n\nЗа первое полугодие 2023 года в Москве было введено в эксплуатацию более 94 тыс. квартир. Каждая квартира, как вы уже поняли, требует согласования. Это значит, что сейчас на рынке перепланировок свободно ❗9,4 млрд. рублей❗, часть из которых ты можешь получить согласовывая перепланировки и сотрудничая с нами!\n\nВот мои рекомендации👇:\n- пройдите обучающий курс «Навык» за 119.900 руб. или «Профессия» за 149.900 руб. (есть рассрочка) и получайте 100 тыс.… 200 тыс.... 300 тыс.… ∞ руб. в месяц на согласованиях, сотрудничая с нами!\n 🌟Лучшие студенты смогут пройти стажировку в нашей команде и получать стабильный поток клиентов от компании!🌟 \nПодробнее по <a href='https://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры.", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
        
    elif message.text == 'Свой вариант ответа 👤':
        bot.send_message(message.from_user.id, "Напишите больше о себе:\nЧем занимаетесь?", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_prof)
        
    else:
        bot.send_message(message.from_user.id, "Для старта напишите /start. \n\nЕсли у вас остались вопросы, свяжитесь с нами по номеру телефона +7 913 970-00-37", reply_markup=types.ReplyKeyboardRemove())
        
    
        
        


def get_name(message):
    x["name"] = message.text
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    reg_button = types.KeyboardButton(text="Поделиться номером", request_contact=True)
    keyboard.add(reg_button)
    bot.reply_to(message, "Приятно познакомиться, " + message.text + "!\n\nУкажите Ваш номер телефона для связи 📞.\n\nДля этого нажмите на кнопку ниже \U00002B07", reply_markup=keyboard)
    bot.register_next_step_handler(message, get_phone)
    
def get_phone(message):
    x["phone"] = message.contact.phone_number
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Я дизайнер 🎨")
    btn2 = types.KeyboardButton("Я риэлтор 📑")
    btn3 = types.KeyboardButton("Я собственник квартиры 🏠")
    btn4 = types.KeyboardButton("Я инвестор в недвижимость 💵")
    btn5 = types.KeyboardButton("Я в поисках дохода 🎯")
    btn6 = types.KeyboardButton("Свой вариант ответа 👤")
    markup.add(btn1).add(btn2).add(btn3).add(btn4).add(btn5).add(btn6)
    bot.reply_to(message, 'Я помощник в команде обучающего курса "Формула перепланировок". А вы?', reply_markup=markup)
    
def get_prof(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Хотел узнать про нормы перепланировок 🧐")
    btn2 = types.KeyboardButton("Искал дополнительный доход 💵")
    btn3 = types.KeyboardButton("Свой ответ")    
    markup.add(btn1).add(btn2).add(btn3)
    bot.reply_to(message, 'Почему вы пришли на курс "Перепланировка без взрыва мозга"?', reply_markup=markup)
    bot.register_next_step_handler(message, get_reason)
    
    
def get_reason(message):
    if message.text == "Хотел узнать про нормы перепланировок 🧐":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.reply_to(message, "Здорово🔥! Я тоже люблю разбираться в нормах законодательства!\n\nВот мои рекомендации👇:\n- пройдите обучающий курс «Коротко о главном в перепланировках» за 19.900 руб. (есть рассрочка), чтобы видеть перепланировки на объектах недвижимости, понимать величину торга, быть авторитетом в глазах клиента.  \nПодробнее по <a href='https://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры",reply_markup=markup, parse_mode='HTML')
    elif message.text == "Искал дополнительный доход 💵":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.reply_to(message, "Отлично🔥! Вы можете стать экспертом и получить новую работу с высоким чеком!\n\nВот мои рекомендации👇:\n- пройдите обучающий курс «Навык» за 119.900 руб. или «Профессия» за 149.900 руб. (есть рассрочка) и получайте 100 тыс.… 200 тыс.... 300 тыс.… ∞ руб. в месяц на согласованиях, работая с нами в команде.\n 🌟Лучшие студенты смогут пройти стажировку в нашей команде и получать стабильный поток клиентов от компании!!🌟 \nПодробнее по <a href='https://formula-ncpr.ru/kurs'>ссылке</a> \n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры", reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)
    else:
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Перепланировки с Анной Страгис»", url='https://t.me/formula_pereplanirovok')
        markup.add(button1)           
        bot.reply_to(message, 'Здорово🔥! Будем на связи!\n\n- нужно будет согласовать перепланировку или захочется стать экспертом в нише с высоким чеком - обращайтесь!\n- подпишитесь на телеграмм канал «Перепланировки с Анной Страгис», там есть и нормы перепланировок, и интересные кейсы, и прямые эфиры', reply_markup=markup)
        
        
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
