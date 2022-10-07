import discord
import asyncio

from discord.ext import commands
from os.path import splitext
from os import listdir

bot = commands.Bot(
    command_prefix='...',
    intents=discord.Intents().all(),
    help_command=None # Disable default discord.py help command.
)

async def load_extensions():
    for filename in listdir("./cogs"):
        await bot.load_extension(f"cogs.{splitext(filename)[0]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start('TOKEN')
 #Code by Daniil Khorava

asyncio.run(main())


