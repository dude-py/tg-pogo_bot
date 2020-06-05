from config import BotConfig as config
from logger import Logger

logger = Logger.getLogger(Logger, "bot.py")
logger.info("Starting")


class Bot:
    """ Клас для взаємодії із зовнішнім світом """
    bot_cmd = {}  # bot command and there function

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

    def setUpdate(self, data):
        """ Цей метод слід викликати коли приходить оновлення на вебхук """
        # parse data
        command = data['result']['bot_command'] if 'bot_command' in data['result'].keys(
        ) else ''

        # run command
        if command in self.bot_cmd.keys():
            self.bot_cmd[command]()

    def addCmd(self, cmd):
        """ декоратор реєстрації команд для бота """
        def wrapped(func):
            self.bot_cmd[cmd] = func
        return wrapped


class BotCmds:
    """ Команди бота """

    Bot = Bot()

    @Bot.addCmd('showme')
    def showme(self):
        """ покаже дані про покемона """
        pass

    @Bot.addCmd('raidbosses')
    def raidbosses(self):
        """ активні рейд боси """
        pass

    @Bot.addCmd('quests')
    def quests(self):
        """ активні квести """
        pass


class BotCmdForAdmins:
    """ адмінка для бота через команди для бота """

    def __init__(self):
        super().__init__()
