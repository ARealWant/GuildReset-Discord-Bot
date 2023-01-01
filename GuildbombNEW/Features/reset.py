import discord


class RESET():
    def __init__(self, interaction: discord.Interaction):
        self.guild = interaction.guild
        self.guild_id = interaction.guild.id
        if len(self.guild.members) > 100:
            print("Guild has more than 100 members, please read the README for more information")
            raise Exception("Guild has more than 100 members, please read the README for more information")
        if not self.guild.me.guild_permissions.administrator:
            print("Bot does not have administrator permission")
            raise Exception("Bot does not have administrator permission")
        if not interaction.user.guild_permissions.administrator:
            print("User does not have administrator permission")
            raise Exception("User does not have administrator permission")

    async def delete_channels(self):
        for channel in self.guild.channels:
            try:
                await channel.delete(reason="Server reset")
            except discord.Forbidden:
                pass

    async def delete_roles(self):
        for role in self.guild.roles:
            try:
                await role.delete(reason="Server reset")
            except discord.Forbidden:
                pass

    async def delete_emojis(self):
        for emoji in self.guild.emojis:
            try:
                await emoji.delete(reason="Server reset")
            except discord.Forbidden:
                pass

    async def delete_webhooks(self):
        for webhook in await self.guild.webhooks():
            try:
                await webhook.delete(reason="Server reset")
            except discord.Forbidden:
                pass

    async def delete_members(self):
        for member in self.guild.members:
            try:
                await member.ban(reason="Server reset")
            except discord.Forbidden:
                pass

    async def delete_all(self):
        await self.delete_channels()
        await self.delete_roles()
        await self.delete_emojis()
        await self.delete_webhooks()
        await self.delete_members()
