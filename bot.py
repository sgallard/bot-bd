import telegram
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
import requests
import time
import datetime


import copy
from parse import urlencode
TOKEN = '627636538:AAET9qgkS7CtQ0VALfsMdu61iI-_60oZS0U'
mi_bot = telegram.Bot(token=TOKEN)
mi_bot_updater = Updater(mi_bot.token)

orden = ["Jose", "Sebastian" , "Bastian"]

now = datetime.datetime.now()
date_of_message = datetime.date(now.year, now.month, now.day)
week = 0







def start(bot=mi_bot, update=mi_bot_updater, orden=orden):
	print "Iniciado el bot"
	print update.message.chat_id
	global week
	orden = ["Jose", "Sebastian" , "Bastian"]
	now = datetime.datetime.now()
	date_of_message = datetime.date(now.year, now.month, now.day)
	week = date_of_message.isocalendar()[1]



	
	print week
	bot.sendMessage(chat_id=update.message.chat_id, text="Holi!!! usa /? para ver los comandos")


def ayuda(bot=mi_bot, update=mi_bot_updater):
 	print "Solicita ayuda"
 	bot.sendMessage(chat_id=update.message.chat_id, text="/start: iniciar con orden Jose, Seba, Basti")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/lab: Mostrar orden de la semana")


# funciones


def reset(bot=mi_bot, update=mi_bot_updater):
	print "bot reiniciado"
	string = str(update.message.text)[7::]

	global week
	global orden
	



	orden = string.strip().split(' ')
	now = datetime.datetime.now()
	date_of_message = datetime.date(now.year, now.month, now.day)
	week = date_of_message.isocalendar()[1]

	print week
	print orden

	bot.sendMessage(chat_id=update.message.chat_id, text="El orden ha sido reiniciado al indicado")

def lab(bot=mi_bot, update=mi_bot_updater):
	
	
	

	
	now = datetime.datetime.now()
	date_of_message = datetime.date(now.year, now.month, now.day)
	cweek = date_of_message.isocalendar()[1]
	

	
	

	if cweek > week:
    	#rotar

		
		global orden
		
		aux = orden[2]
		orden[2] = orden[1]
		orden[1] = orden[0]
		orden[0] = aux

		global week
		week = cweek
		
			
			

	
	bot.sendMessage(chat_id=update.message.chat_id, text="Martes/Jueves: "+ orden[0])
	bot.sendMessage(chat_id=update.message.chat_id, text="Martes: "+ orden[1] + " (Tentativo)")
	bot.sendMessage(chat_id=update.message.chat_id, text="Jueves: "+ orden[2] + " (Tentativo)")


	










#Creamos nuestra instancia "mi_bot" a partir de ese TOKEN




#Definimos para cada comando la funcion que atendera la peticion
start_handler = CommandHandler('start', start)
ayuda_handler = CommandHandler('?', ayuda)
reset_handler = CommandHandler('reset',reset)
orden_handler = CommandHandler('lab', lab)


dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(reset_handler)
dispatcher.add_handler(orden_handler)


mi_bot_updater.start_polling()

while True: #Ejecutamos nuestro programa por siempre
    pass


