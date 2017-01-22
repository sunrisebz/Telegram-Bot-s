# -*- coding: utf-8 -*-
import config
import telebot
import smtplib
import grab
import lxml.html as html
import vk_api


from email.mime.text import MIMEText


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello, Input you phone number and password.Example: Phone:Password')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def vk_comment(message):
    global login, password
    vk_log = message.text
    (login, password) = vk_log.split(':')

    def two_factor_handler():
        code = input('Input secret code')
        return code, False

    if login and password != ' ':
        vk_session = vk_api.VkApi(login, password, auth_handler=two_factor_handler)
        try:
            vk_session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api()
        response = vk.board.addTopic(group_id=127727264, title='New Title', tezt='hello')  # Используем метод wall.get
        if response['items']:
             print(response['items'][0])


if __name__ == "__main__":
    bot.polling(none_stop=True)
