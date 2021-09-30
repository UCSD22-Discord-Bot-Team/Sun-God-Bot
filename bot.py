import os
from dotenv import load_dotenv

import discord
from discord.ext import tasks
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Allows bot to see all members in guild
# also have to enable a setting on developer portal
intents = discord.Intents.default()
intents.members = True
bot = Bot(command_prefix="placeholder", intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded cog '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load cog {extension}\n{exception}")

@bot.event
async def on_command_error(ctx, error):
    raise error

bot.run(TOKEN)
