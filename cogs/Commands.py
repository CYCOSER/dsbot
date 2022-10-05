import discord
from discord.ext import commands
import asyncio


class User_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(move_members=True)
    async def wakeup(self, ctx, member: discord.Member):
        channel = member.voice.channel.id
        for x in range(4):
            await member.move_to(self.bot.get_channel(1027269360764604446))
            await asyncio.sleep(0.5)
            await member.move_to(self.bot.get_channel(1027269419166077008))
        else:
            await member.move_to(self.bot.get_channel(channel))
            print(f"tried to wakeup <<{member.name}>> in <<{self.bot.get_channel(channel)}>> of <<{member.guild}>>")


async def setup(bot):
    await bot.add_cog(User_commands(bot))
