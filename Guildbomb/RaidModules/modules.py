'  The Imports (Do not change anything right here)  '
from UtilsDirectory.data import *


class RaidModules(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["allkick"])
    async def all_kick(self, ctx):
        await ctx.send(f"Kick everyone out of `{ctx.guild.name}`? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    await ctx.send(waitmsg)
                    for user in list(ctx.guild.members):
                        try:
                            await ctx.guild.kick(user)
                        except Exception:
                            pass
                    await ctx.send(donemsg)
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return

    @commands.command(aliases=["allban"])
    async def all_ban(self, ctx):
        await ctx.send(f"Ban everyone out of `{ctx.guild.name}`? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    await ctx.send(waitmsg)
                    for user in ctx.guild.members:
                        try:
                            await ctx.guild.ban(user)
                        except Exception:
                            pass
                    await ctx.send(donemsg)
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return

    @commands.command(aliases=["allrename"])
    async def all_rename(self, ctx, newname):
        await ctx.send(f"Rename everyone to `{newname}` in `{ctx.guild.name}`? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    await ctx.send(waitmsg)
                    for user in list(ctx.guild.members):
                        try:
                            await user.edit(nick=newname)
                        except Exception:
                            pass
                    await ctx.send(donemsg)
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return

    @commands.command(aliases=["senddm", "alldm"])
    async def all_dm(self, ctx, message):
        await ctx.send(f"DM everyone with `{message}` in `{ctx.guild.name}`? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    await ctx.send(waitmsg)
                    for user in list(ctx.guild.members):
                        try:
                            await user.send(nick=message)
                        except Exception:
                            pass
                    await ctx.send(donemsg)
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return

    @commands.command(aliases=["delemojis"])
    async def del_emojis(self, ctx):
        await ctx.send(f"Delete every emoji in `{ctx.guild.name}`? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    await ctx.send(waitmsg)
                    for emoji in list(ctx.guild.emojis):
                        try:
                            await emoji.delete()
                        except Exception:
                            pass
                    await ctx.send(donemsg)
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return

    @commands.command(aliases=["delinvites"])
    async def del_invites(self, ctx):
        await ctx.send(f"Delete every invite in `{ctx.guild.name}`? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    await ctx.send(waitmsg)
                    for invite in await ctx.guild.invites():
                        try:
                            await invite.delete()
                        except Exception:
                            pass
                    await ctx.send(donemsg)
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return

    @commands.command(aliases=["delchannels"])
    async def del_channels(self, ctx):
        await ctx.send(f"Delete every channel in `{ctx.guild.name}`? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    await ctx.send(waitmsg)
                    for channels in list(ctx.guild.channels):
                        try:
                            await channels.delete()
                        except Exception:
                            pass
                    await ctx.author.send(donemsg)
                    return
                await ctx.send(waitmsg)
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return

    @commands.command(aliases=["delroles"])
    async def del_roles(self, ctx):
        global wait
        await ctx.send(f"Delete every role in `{ctx.guild.name}`? [y/n]")

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = await self.bot.wait_for('message', check=check_data, timeout=int(timeout))
                if msg.content == "y":
                    wait = await ctx.send(waitmsg)
                    for roles in list(ctx.guild.roles):
                        try:
                            await roles.delete()
                        except Exception:
                            pass
                    await ctx.send(donemsg)
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return


def setup(bot):
    bot.add_cog(RaidModules(bot))
