import telebot
import logging
from decouple import config

###############################

#Version del bot
VERSION = 1.0

# Obtiene el token desde el archivo de configuración
TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')
#########################################################
# Crea el objeto bot utilizando el token
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Determina el nivel de los mensajes que se van a mostrar (debug)
telebot.logger.setLevel(logging.INFO)
#########################################################