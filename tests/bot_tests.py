import disnake
from disnake.ext import commands
from disnake.ext.commands import InteractionBot

from os import getenv
from dotenv import load_dotenv
load_dotenv()
from typing import List

intents = disnake.Intents.default()
intents.members = True

class Bot(InteractionBot):

    def __init__(self):

        self.test_mode = bool(getenv("TEST_GUILD"))
        self.cog_not_loaded: List[str] = []

        if self.test_mode:
            print("Starting Bot in debug mode...")
            super().__init__(intents=intents, test_guilds=[int(getenv("TEST_GUILD"))])
        else:
            print("Starting Bot in prod mode...")
            super().__init__(intents=intents)

        #self.load_commands()

bot = Bot()