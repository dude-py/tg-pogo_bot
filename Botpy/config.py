from os import getenv

class BotConfig:
    tg_url = "https://api.telegram.org/"
    tg_webhook = "https://26da12afac08.ngrok.io"
    tg_api_key = getenv("tg_api_key")
    