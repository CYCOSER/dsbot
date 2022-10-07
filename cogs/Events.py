import discord
import asyncio

from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('-----------------------------------------------------------------------------------')
        print(f"logged in as {self.bot.user.name}")
        print(f"id: {self.bot.user.id}")
        print(f"connected to: {list(self.bot.guilds)[0]}")
        for i in range(len(list(self.bot.guilds)) - 1):
            print(f"              {list(self.bot.guilds)[i + 1]}")
        print('-----------------------------------------------------------------------------------')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(608673993658073098)
        channel = guild.get_channel(608688631485300741)
        await asyncio.sleep(1)
        embed = discord.Embed(
            title=f"{member.name}, please select games you play by clicking here",
            description="It will send you to the roles channel",
            url="https://discord.com/channels/608673993658073098/1023545339342508096",
            color=0xf1c40f
        )
        await channel.send(f"Welcome to the server {member.mention}! :partying_face:")
        await member.send(embed=embed)
        await member.send(f"Welcome to the {guild.name} server, {member.name}! :partying_face:")
        print(f"<<{member.name}>> has joined <<{member.guild}>>")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1023332736376770611)
        await channel.send(f"{member.mention} has left us :disappointed_relieved:, but we keep going")
        print(f"<<{member.name}>> has left <<{member.guild}>>")


async def setup(bot):
    await bot.add_cog(Events(bot))
