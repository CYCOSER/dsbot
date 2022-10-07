import discord

from discord.ext import commands


class Role_adder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emojis_roles_arr = [["🇱", "♿", "🇫", "🅰️", "🇵", "🧗", "🏜️", "⚽", "🔫", "🇻"],
                                 ["LOL", "DOTA 2", "Fortnite", "APEX", "PUBG", "Genshin", "BDO", "Rocket league",
                                  "CS_GO", "Valorant"]]

    @commands.Cog.listener()
    async def on_ready(self, txt=""):
        channel = self.bot.get_channel(1023545339342508096)
        toggle = 0
        if toggle == 1:
            channel.purge()
            for x in range(len(self.emojis_roles_arr[0])):
                txt += f"\n\n{self.emojis_roles_arr[0][x]} - {self.emojis_roles_arr[1][x]}"
            msg = await channel.send(f"React emojis of games you play:{txt}")
            for i in range(len(self.emojis_roles_arr[0])):
                await msg.add_reaction(self.emojis_roles_arr[0][i])

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        messageId = 1025782368180637716
        if messageId == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            for i in range(len(self.emojis_roles_arr[0])):
                if emoji == self.emojis_roles_arr[0][i]:
                    role = discord.utils.get(guild.roles, name=self.emojis_roles_arr[1][i])
            await member.add_roles(role)
            print(f"gave <<{member.name}>> in <<{guild}>> server <<{role}>> role through reaction")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        messageId = 1025782368180637716
        if messageId == 1025782368180637716:
            guild = await(self.bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            for i in range(len(self.emojis_roles_arr[0])):
                if emoji == self.emojis_roles_arr[0][i]:
                    role = discord.utils.get(guild.roles, name=self.emojis_roles_arr[1][i])
            member = await(guild.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
            print(f"removed <<{role}>> role from <<{member.name}>> in <<{guild}>> server cuz (s)he removed reaction")


async def setup(bot):
    await bot.add_cog(Role_adder(bot))
