# -*- coding: utf-8 -*-
import logging
import os
from typing import List

import disnake
from disnake.ext import commands

from .bot import Bot

logger = logging.getLogger("bot")


class AdminAddUserModal(disnake.ui.Modal):

    _email_default_value = "N/A"

    #! TODO: use locale strings
    
    def __init__(self, user: disnake.User) -> None:
        self.user = user
        components = [
            disnake.ui.TextInput(label=f"Prenom + Nom", custom_id="name"),
            disnake.ui.TextInput(label="Adresse email (optional)", custom_id="email", required=False),
        ]
        super().__init__(title=f"Ajout d'un utilisateur", components=components, timeout=10 * 60)

    async def callback(self, interaction: disnake.ModalInteraction, /) -> None:
        await interaction.response.defer(ephemeral=True)
        name = interaction.text_values.get("name")
        email = interaction.text_values.get("email")
        if email == "":
            email == self._email_default_value
        #Database.set_user(self.user, name, email)
        await interaction.edit_original_response(
            embed=disnake.Embed(
                description=f"{self.user.mention} a bien été ajouté.e à la base de donnée", color=disnake.Color.green()
            )
        )

        #await update_user(self.user, name=name)