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

HISTORY_LIMIT = 200

@bot.slash_command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.slash_command(
        default_member_permissions=disnake.Permissions.all(),
        dm_permission=False
)
async def send_register_message_here(ctx):
    channel = ctx.channel
    view = disnake.ui.View()
    button = disnake.ui.Button(label='Register', url=f"{getenv('SITE_URL')}", style=disnake.ButtonStyle.link)
    view.add_item(button)
    #await channel.send("Use this link to register:", view=view)
    #await ctx.send("Message sent!", ephemeral=True)
    channel_dropdown = disnake.ui.ChannelSelect() # FIXME: This is not working yet: https://guide.disnake.dev/interactions/select-menus#example-of-stringselects
    channel_dropdown.callback = func # ?
    await ctx.send("Choose a channel to send the register message:", view=channel_dropdown)
    print(channel_dropdown.values[0])

async def func():
    print("Selected channel")



async def check_bot_message_doesnt_exists(channel: disnake.TextChannel) -> bool:
    pinned_messages = await channel.pins()
    for message in pinned_messages:
        if message.author == bot.user:
            print(message)
            print(message.content)
            return False
    async for message in channel.history(limit=HISTORY_LIMIT):
        if message.author == bot.user:
            print(message)
            print(message.content)
            return False
    return True

@bot.event
async def on_ready():
    CHANNEL_ID = int(getenv("TEST_CHANNEL"))
    channel = bot.get_channel(CHANNEL_ID)
    view = disnake.ui.View()
    sending_register_button = False
    if channel:
        # Check if there's already a message from the bot in the channel
        if await check_bot_message_doesnt_exists(channel):
            button = disnake.ui.Button(label='Register', url=f"{getenv('SITE_URL')}", style=disnake.ButtonStyle.link)
            view.add_item(button)
            sending_register_button = True
        else:
            print("A message from the bot already exists in the channel.")
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")

    if sending_register_button:
        try:
            sent_message = await channel.send("Use this link to register:", view=view)
        except disnake.errors.Forbidden:
            print("Could not send the message, the bot does not have the permission to send messages.")
        try:
            await sent_message.pin()
        except disnake.errors.Forbidden:
            print("Could not pin the message, the bot does not have the permission to pin messages.")

print("Running bot...")
bot.run(getenv("DISCORD_BOT_TOKEN"))

bot.close()
