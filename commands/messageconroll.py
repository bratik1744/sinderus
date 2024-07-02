from random import choice
from telebot import types
from database import *



def messagecontroll(message, bot):
    id = message.from_user.id
    text = message.text
    if text == '/start':
        if search_acc(telegram_id=id):
            bot.send_message(id, f"Привет, я бот для знакомств в сириусе, для начала мы заполним данные о тебе, как тебя зовут?")
            edit_acc(telegram_id=id, id_last_commands=0)

        else:
            bot.send_message(id, f"Привет, я бот для знакомств в сириусе, для начала мы заполним данные о тебе, как тебя зовут?")
            new_user(telegram_id=id, username=message.from_user.username)
        return

    last_id: int = search_acc(telegram_id=id)[0][2]
    if last_id == 0:
        edit_acc(telegram_id=id, name=text, id_last_commands=1)
        bot.send_message(id, "Сколько тебе лет?")
    elif last_id == 1:
        if text.isdigit():
            edit_acc(telegram_id=id, old=int(text), id_last_commands=2)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Я парень")
            item2 = types.KeyboardButton("Я девушка")
            markup.add(item1)
            markup.add(item2)
            bot.send_message(id, "Теперь определимся с полом.", reply_markup=markup)
        else:
            bot.send_message(id, "Ой, что-то не то.")
    elif last_id == 2:
        if text == "Я парень":
            edit_acc(telegram_id=id, gender="male", id_last_commands=3)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Наука")
            item2 = types.KeyboardButton("Искусство")
            item3 = types.KeyboardButton("Спорт")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(id, "На каком ты направлении?", reply_markup=markup)

        elif text == "Я девушка":
            edit_acc(telegram_id=id, gender="female", id_last_commands=3)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Наука")
            item2 = types.KeyboardButton("Искусство")
            item3 = types.KeyboardButton("Спорт")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(id, "На каком ты направлении?", reply_markup=markup)

        else:
            bot.send_message(id, "Ой, что-то не то.")

    elif last_id == 3:
        if text in ["Наука", "Искусство", "Спорт"]:
            edit_acc(telegram_id=id, direction=text, id_last_commands=4)

            markup = types.ReplyKeyboardRemove()
            bot.send_message(id, "Расскажи о себе и кого хочешь найти, чем предлагаешь заняться. Это поможет лучше подобрать тебе компанию.", reply_markup=markup)

        else:
            bot.send_message(id, "Ой, что-то не то.")
    elif last_id == 4:
        edit_acc(telegram_id=id, description=text, id_last_commands=5)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Парни")
        item2 = types.KeyboardButton("Девушки")
        item3 = types.KeyboardButton("Все равно")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(id, "Кто тебе интересен?", reply_markup=markup)

    elif last_id == 5:
        markup = types.ReplyKeyboardRemove()
        if text == "Парни":
            edit_acc(telegram_id=id, gender_interests="male", id_last_commands=6)
            bot.send_message(id, "Теперь пришли фото", reply_markup=markup)
        elif text == "Девушки":
            edit_acc(telegram_id=id, gender_interests="female", id_last_commands=6)
            bot.send_message(id, "Теперь пришли фото", reply_markup=markup)
        else:
            edit_acc(telegram_id=id, id_last_commands=6)
            write_None(telegram_id=id)
            bot.send_message(id, "Теперь пришли фото", reply_markup=markup)
    elif last_id == 7:
        if text == "Заполнить анкету заново":
            markup = types.ReplyKeyboardRemove()
            bot.send_message(id, "как тебя зовут?", reply_markup=markup)
            edit_acc(telegram_id=id, id_last_commands=0)
        elif text == "Смотреть анкеты" or text == "Пропустить":
            ank = search_anket(search_acc(telegram_id=id)[0][8])
            lst = set([i[0] for i in ank])
            lst_view = set(search_acc(telegram_id=id)[-1].split())
            vib = lst - lst_view

            if vib:
                ank_id = choice(list(vib))
                acc = search_acc(telegram_id=ank_id)[0]
                text = f"""\n{acc[3]}, {acc[4]}, {acc[5]}, {acc[6]}.\n{acc[7]}"""
                f = open(fr"database\photo\{ank_id}.jpg", 'rb')
                print(fr"database\photo\{ank_id}.jpg")

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Лайкнуть")
                item2 = types.KeyboardButton("Пропустить")
                item3 = types.KeyboardButton("Заполнить анкету заново")
                item4 = types.KeyboardButton("Проверить лайки")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                bot.send_photo(id, f, caption=text, reply_markup=markup)
                edit_acc(telegram_id=id, id_like=ank_id)
                edit_view(id, ank_id)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Смотреть анкеты")
                item2 = types.KeyboardButton("Заполнить анкету заново")
                item3 = types.KeyboardButton("Проверить лайки")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                bot.send_message(id, "ой, доступные анкеты закончились", reply_markup=markup)

        elif text == "Лайкнуть":
            new_like(telegram_id_who=id, telegram_id_whom=search_acc(telegram_id=id)[0][9])

            ank = search_anket(search_acc(telegram_id=id)[0][8])
            lst = set([i[0] for i in ank])
            lst_view = set(search_acc(telegram_id=id)[-1].split())
            vib = lst - lst_view
            if vib:
                ank_id = choice(list(vib))
                acc = search_acc(telegram_id=ank_id)
                text = f"""\n{acc[3]}, {acc[4]}, {acc[5]}, {acc[6]}.\n{acc[7]}"""
                f = open(fr"database\photo\{ank_id}.jpg", 'rb')

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Лайкнуть")
                item2 = types.KeyboardButton("Пропустить")
                item3 = types.KeyboardButton("Заполнить анкету заново")
                item4 = types.KeyboardButton("Проверить лайки")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                bot.send_photo(id, f, caption=text, reply_markup=markup)
                edit_acc(telegram_id=id, id_like=ank_id)
                edit_view(id, ank_id)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Смотреть анкеты")
                item2 = types.KeyboardButton("Заполнить анкету заново")
                item3 = types.KeyboardButton("Проверить лайки")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                bot.send_message(id, "ой, доступные анкеты закончились", reply_markup=markup)
        elif text == "Проверить лайки":
            lst = mylike(telegram_id=id)
            for i in lst:
                iid = i[0]
                acc = search_acc(telegram_id=iid)[0]
                text = f"""{acc[3]}, {acc[4]}, {acc[5]}, {acc[6]}, @{acc[1]}.\n{acc[7]}"""
                f = open(fr"database\photo\{iid}.jpg", 'rb')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Смотреть анкеты")
                item2 = types.KeyboardButton("Заполнить анкету заново")
                item3 = types.KeyboardButton("Проверить лайки")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                bot.send_photo(id, f, caption=text, reply_markup=markup)
        else:
            bot.send_message(id, "ой, что-то не то")
    else:
        bot.send_message(id, "ой, ой, ой, что-то сильно не так")

