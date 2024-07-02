from telebot import TeleBot
from commands import messagecontroll
from database import edit_acc
from database import search_acc
from telebot import types


token = "7393466745:AAFDmWgnjE3mRpave_3OcgBWdaJeUJFDqEs"
bot = TeleBot(token=token)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    messagecontroll(message, bot)


@bot.message_handler(content_types=['photo'])
def photo(message):
    last_id: int = search_acc(telegram_id=message.from_user.id)[0][2]
    if last_id == 6:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        print(f"photo id = {message.from_user.id}")
        edit_acc(telegram_id=message.from_user.id, completed=1, id_last_commands=7)
        with open(f"database/photo/{message.from_user.id}.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        acc = search_acc(telegram_id=message.from_user.id)[0]
        text = f"""Отлично, так выглядит твоя анкета:\n{acc[3]}, {acc[4]}, {acc[5]}, {acc[6]}.\n{acc[7]}"""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Смотреть анкеты")
        item2 = types.KeyboardButton("Заполнить анкету заново")
        markup.add(item1)
        markup.add(item2)
        bot.send_photo(message.from_user.id, downloaded_file, caption=text, reply_markup=markup)



def starbot():
    bot.infinity_polling()


if __name__ == "__main__":
    starbot()

