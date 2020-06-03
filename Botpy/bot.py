from config import BotConfig as config
from logger import Logger

logger = Logger.getLogger(Logger, "bot.py")
logger.info("Starting")


class Bot:
    """ Клас для взаємодії із зовнішнім світом """

    def __init__(self):
        from BotApi import getWebhookInfo, setWebhook
        # Check webhook
        webhook_info = getWebhookInfo()
        if('url' in webhook_info['result'].keys()):
            result = (config.tg_webhook != webhook_info['result']['url']) or (
                len(webhook_info['result']['url']) == 0)
            if(result):
                logger.info("setting webhook {}".format(config.tg_webhook))
                setWebhook(config.tg_webhook)
            logger.info("webhook alredy set")

    def setUpdate(self):
        """ Цей метод слід викликати коли приходить оновлення на вебхук """
        pass
