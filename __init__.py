import telepot, time, subprocess
from botpy import  last_letter
from syllables import syllables

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	if (content_type == 'text'):
		command = msg['text']
		bot.sendMessage(chat_id, last_letter(command))				

f = open('token', 'r')
token=f.read()
f.close()

bot = telepot.Bot(token)
bot.message_loop(handle)


while 1:
    time.sleep(20)