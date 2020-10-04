import telebot
import os
import json

"""
Init Telegram bot.
You have to set Lambda environment variables:
TOKEN - your bot Telegram API token
WEBHOOK_URL - your AWS API Gateway HTTP url
"""

TOKEN = os.getenv ('TOKEN')
WEBHOOK_URL = os.getenv ('WEBHOOK_URL')
bot = telebot.TeleBot (TOKEN, threaded=False)
bot.set_webhook (WEBHOOK_URL)

def lambda_handler (event, context):
    """
    Lambda handler. Just replay the almost the same text.
    """
    
    body = json.loads (event['body'])
    message = body['message']
    bot.send_message (message["chat"]["id"], 'Hey!\nYou said: ' + message["text"])
    return {
        'statusCode': 200
    }
