import requests
import json.encoder

from config import BotConfig
from logger import Logger

logger = Logger.getLogger(Logger, "BotApi.py")
logger.info("Starting")

tg_url = BotConfig.tg_url + 'bot' + BotConfig.tg_api_key + '/'


def getMe():
    """
    A simple method for testing the bot auth token.
    Requires no parameters. Return basic information about the bot.
    return = dict obj
    """
    url = tg_url + "getMe"
    return(
        json.loads(requests.get(url).text)
    )


def sendMesg(chat_id, text):
    """ Use this method to send text messages. On success, the sent Message is returned.
    chat_id = Unique identifier for the target chat or username
    text = Text of the message to be sent
    return = dict obj
    """
    url = tg_url + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    return(
        json.loads(requests.get(url).text)
    )


def sendPhoto(chat_id, photo, caption=""):
    """ Use this method to send photos. On success, the sent Message is returned.
    chat_id = Unique identifier for the target chat or username
    photo = Photo to send. Pass a file_id as String to send a photo that exists
            on the Telegram servers (recommended), pass an HTTP URL as a String
            for Telegram to get a photo from the Internet
    caption = Photo caption
    return = dict obj
    """
    url = tg_url + "sendPhoto?chat_id{}".format(chat_id)
    return(
        json.loads(requests.get(url).text)
        )


def setWebhook(url="", max_connections=40):
    """ Use this method to specify a url and receive incoming updates via an outgoing webhook. 
    return = dict obj
    """
    webhook = tg_url + "setWebhook?url={}".format(url)
    return(json.loads(
        requests.get(webhook).text)
    )


def getWebhookInfo():
    """ Use this method to get current webhook status.
    If the bot is using getUpdates, will return an object with the url field empty.
    return = dict obj
    """
    url = tg_url + "getWebhookInfo"
    return(json.loads(
        requests.get(url).text
    ))