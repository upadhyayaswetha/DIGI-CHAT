#importing libraries

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os 

#defining name of chatbot and defining name of trainer

bot=ChatBot('PINKY')
bot.set_trainer(ListTrainer)

#accesing chatterbot corpus

for files in os.listdir('C:/Users/DELL/Desktop/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('C:/Users/DELL/Desktop/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)

while True:
    message=input('You:')
    if message.strip!='Bye' or message.strip!='bye':
        reply=bot.get_response(message)
        print('ChatBot:',reply)
    if message.strip=='Bye' or message.strip=='bye':
        print('PINKY:It was nice talking to you, CHEERIO')
        break
