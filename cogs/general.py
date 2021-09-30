import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="ping",
        description="Check if the bot is alive.",
        guild_ids=[592923725884686355],
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