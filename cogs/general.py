import json
import os
import sys

import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="ping",
        description="Check if the bot is alive.",
    )
    async def ping(self, ctx: SlashContext):
        """
        Check if the bot is alive.
        """

        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"The bot latency is {round(self.bot.latency * 1000)}ms.",
            color=0x42F56C
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(general(bot))