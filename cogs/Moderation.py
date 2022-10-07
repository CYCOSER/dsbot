import asyncio

from discord.ext import commands
from discord.ext.commands import has_permissions


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='clear',
        aliases=['c', 'purge'], # May be used instead of default command name to invoke this command.
        help="|this command will clear X (5 by default) amount of messages"
    )
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.send(f"Clearing {amount} messages in 1 sec")
        await asyncio.sleep(0.5)
        await ctx.channel.purge(limit=amount + 2)
        print(f"cleared {amount} messages in <<{ctx.channel}>> channel of <<{ctx.guild}>>")

    @commands.command(name='fullClear', help='|wipes all the messages in current channel')
    @has_permissions(manage_messages=True)
    async def fullClear(self, ctx):
        await ctx.send("wiping process:")
        msg = await ctx.send("0%")
        await asyncio.sleep(0.5)
        for countdown in range(1, 100, 37):
            await msg.edit(content=f"{countdown}%")
            await asyncio.sleep(0.1)
        else:
            await msg.edit(content="100%")
        await ctx.channel.purge()
        print(f"wiped messages in <<{ctx.channel}>> channel of <<{ctx.guild}>>")


async def setup(bot):
    await bot.add_cog(Moderation(bot))
