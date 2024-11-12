# -*- coding: utf-8 -*-
import logging
import os
from os import getenv
from dotenv import load_dotenv
load_dotenv()
from typing import List

import disnake
from disnake.ext import commands

from .bot import Bot

logger = logging.getLogger("bot")

#! TODO: use locale strings
class RegisterButton(disnake.ui.Button):
    
    def __init__(self, user: disnake.User) -> None:
        super().__init__(style=disnake.ButtonStyle.link, url=f"{getenv("SITE_URL")}", label=f"Register")
        self.user = user

    """
    async def callback(self, interaction: disnake.MessageInteraction, /) -> None:
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_message(
            embed=disnake.Embed(
                description=f"{self.user.mention} has been registered", color=disnake.Color.green()
            )
        )
    """


