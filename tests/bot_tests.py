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

        self.cog_not_loaded: List[str] = []

        print("Starting Bot in debug mode...")
        super().__init__(intents=intents, test_guilds=[int(getenv("TEST_GUILD"))])

        #self.load_commands()

bot = Bot()

@bot.event
async def on_ready():
    channel = bot.get_channel(int(getenv("TEST_CHANNEL")))
    if channel:
        button = disnake.ui.Button(label="Register", url=f"{getenv('SITE_URL')}", style=disnake.ButtonStyle.link)
        view = disnake.ui.View()
        view.add_item(button)
        await channel.send("Here is a link button:", view=view)
