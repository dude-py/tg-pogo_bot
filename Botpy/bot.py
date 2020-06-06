from Botpy.config import BotConfig as config
from Botpy.logger import Logger

logger = Logger.getLogger(Logger, "bot.py")
logger.info("Starting")


class Bot:
    """ Клас для взаємодії із зовнішнім світом """
    bot_cmd = {}  # bot command and there function

    def __init__(self):
        from Botpy.BotApi import getWebhookInfo, setWebhook
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
            return func
        return wrapped


class BotCmds(object):
    """ Команди бота """

    Bot = Bot()

    def _execute(self, sql_query):
        """ метод для роботи з бд. На вхід приймиє sql_query,
        на виході поверне масив контежів
        sql_query = str, sql query
        """
        import pymysql
        conn = pymysql.connect(host="localhost", user="tony",
                               password="password", db="testdb", charset="utf8")
        try:
            with conn.cursor() as cursor:
                c = cursor.execute(sql_query)
                print("c == " + str(c))
                result = [row for row in cursor]
                return result
        except pymysql.Error as e:
            logger.info("MySQL error: " + str(e))
        finally:
            conn.close()

    def _parse_raw_data(self, raw_data, schema):
        """ парсить сирі дані з бд. повертає list of dicts """
        result = []

        for row in raw_data:
            i = 0
            tmp = {}
            for data in row:
                tmp[schema[i]] = data
                i += 1
            result.append(tmp)
        return result

    @Bot.addCmd('showme')
    def showme(self, pkm_name):
        """ покаже дані про покемона """
        # 1.сходити в бд за даними
        sql_query = "SELECT * FROM pokedex WHERE pokemon_name='{}'".format(
            pkm_name)
        raw_data = self._execute(sql_query)
        # 2. спарсити сирі дані.
        schema = ['id', 'pokemon_id', 'pokemon_name', 'form', 'types',
                  'base_attack', 'base_defense', 'base_stamina', 'file_id']
        pretty_data = self._parse_raw_data(raw_data, schema)
        pretty_data = pretty_data[0]
        # 3. передати в BotApi.sendPhoto()
        caption = "name: {}\ntype: {}\nbase atk: {}\n -*- def: {}\n -*- sta: {}"
        caption = caption.format(pretty_data['pokemon_name'], pretty_data['types'], pretty_data['base_attack'],
                                 pretty_data['base_defense'], pretty_data['base_stamina'])

        print(caption)

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
