from imap_tools import MailBox, AND
from telebot import TeleBot
from mytoken import TeleToken, PassVini
from rich import print
from time import sleep
import pyfiglet
import os

os.system('clear')
user = 'YOUR_EMAIL'
bot = TeleBot(TeleToken())

banner = pyfiglet.figlet_format('AlertBot')
print(f'[bold]{banner}[/]')
print(' [blue][Bot] - Connected![/]')

class EmailAlert:
    @bot.message_handler(commands=['start'])
    def Gmail(message):
        while True:
            with MailBox('imap.gmail.com').login(user, PassVini()) as inbox:
                for msg in inbox.fetch(AND(seen=False)):
                    print(f'\n\nNova mensagem de {msg.from_}')
                    data = msg.date
                    hora = msg.date
                    bot.send_message(message.chat.id, 
                        f'''---------- ☾ 🤖 NOVO EMAIL 🤖☽ ----------\n\n
                            *From:* {msg.from_}\n
                            *Subject:* {msg.subject.title()}\n
                            *Date:* {str(data)[:10].replace('-', '/')} ás {str(hora)[11:16]}''', 
                            parse_mode='Markdown'
                                )
                    with open('Message.txt', 'a') as mensagem:
                        mensagem.writelines(
                            f'------ Message ------\n\n{msg.text}'
                                )
                    sleep(0.8)
                    bot.send_document(message.chat.id, open(
                        'Message.txt'), 'rb'
                            )

                    mensagem.close()
                    os.system('rm -rf Message.txt')

    bot.infinity_polling()

vini = EmailAlert()
vini.Gmail()
        