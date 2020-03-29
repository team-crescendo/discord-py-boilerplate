import json
import logging
import logging.config
import os

from discord.ext import commands
from dotenv import load_dotenv

with open("logging.json") as f:
    logging.config.dictConfig(json.load(f))


logger = logging.getLogger("bot")
load_dotenv()


class DiscordBot(commands.Bot):
    extension_list = ["extensions.admin"]

    async def on_ready(self):
        logger.info(f"Logged in as {self.user}")

    async def on_error(self, event, *args, **kwargs):
        logger.exception("")

    def __init__(self):
        super().__init__(commands.when_mentioned_or("!"))
        for ext in self.extension_list:
            self.load_extension(ext)


bot = DiscordBot()


bot.run(os.getenv("BOT_TOKEN"))
