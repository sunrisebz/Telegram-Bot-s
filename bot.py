# -*- coding: utf-8 -*-
import config
import telebot
import smtplib
import grab
import lxml.html as html
import vk


from email.mime.text import MIMEText


bot = telebot.TeleBot(config.token)

i = 0
ch2 = 0


@bot.message_handler(regexp='/help')
def command_help(message, ):
    global ch2
    i = bot.send_message(message.chat.id, 'Welcome to sunrise support, describe your problem')
    i = int(ch2)
    ch2 += 1

    while ch2 == 1:
        bot.send_message(message.chat.id, 'Write you message and sand him to me')
        ch2 += 1


@bot.message_handler(func=lambda message: True, content_types=['text'])
def help(message):
    global ch2
    if ch2 == 2:
        me = 'sunrise.programm@gmail.com'  # отправитель
        you = 'support@sunrisebz.pro'  # получатель
        text = message.text  # текст письма
        subj = 'Telegram Comment bot Support '  # заголовок письма
        # SMTP-сервер
        server = "smtp.gmail.com"
        port = 25
        user_name = "sunrise.programm@gmail.com"
        user_password = "BaNdIt228"
        # формирование сообщения
        msg = MIMEText(text, "", "utf-8")
        msg['Subject'] = subj
        msg['From'] = me
        msg['To'] = you
        # отправка
        send = smtplib.SMTP(server, port)
        send.ehlo()
        send.starttls()
        send.ehlo()
        send.login(user_name, user_password)
        send.sendmail(me, you, msg.as_string())
        send.quit()
        bot.send_message(message.chat.id, 'You answer send')
        ch2 = 0


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    'https://oauth.vk.com/authorize?client_id={ID = 5815183}&display=mobile&&redirect_uri=https://oauth.vk.com/blank.html&scope=manage,offline'







if __name__ == "__main__":
    bot.polling(none_stop=True)
