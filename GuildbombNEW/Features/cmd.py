import asyncio

import nextcord
from nextcord import app_commands
from discord.app_commands import Group
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from Features.reset import RESET


class CMD(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("EXTENSION LOADED: RAID MODULE SUCCESSFULLY LOADED")

    reset = Group(name='start', description='Start a reset')

    @reset.command(name="channels", description="Start a channel reset")
    @app_commands.describe(confirm="Confirm the deletion of all channels in the server")
    async def channels(self, interaction: discord.Interaction, confirm: bool = False):
        '''
        Deletes all channels in the guild
        :param interaction: The interaction object
        :param confirm: Whether or not to confirm the action
        '''
        if confirm:
            try:
                reset = RESET(interaction)
                await reset.delete_channels()
                return await interaction.response.send_message("> ***✅ All channels have been successfully "
                                                               "deleted from the server {}***".format(
                    interaction.guild.name))
            except Exception as e:
                await interaction.response.send_message(f"> ***❌ ERROR: {e}***", ephemeral=True)
                return print(f"ERROR: {e}")
        else:
            return await interaction.response.send_message(
                "> ***❌ This command requires confirmation. Please run the command "
                "again with the confirm argument set to True***", ephemeral=True)

    @reset.command(name="roles", description="Start a role reset")
    @app_commands.describe(confirm="Confirm the deletion of all roles in the server")
    async def roles(self, interaction: discord.Interaction, confirm: bool = False):
        '''
        Deletes all roles in the guild
        :param interaction: The interaction object
        :param confirm: Whether or not to confirm the action
        '''
        if confirm:
            try:
                reset = RESET(interaction)
                await reset.delete_roles()
                return await interaction.response.send_message("> ***✅ All roles have been successfully "
                                                               "deleted from the server {}***".format(
                    interaction.guild.name))
            except Exception as e:
                await interaction.response.send_message(f"> ***❌ ERROR: {e}***", ephemeral=True)
                return print(f"ERROR: {e}")
        else:
            return await interaction.response.send_message(
                "> ***❌ This command requires confirmation. Please run the command "
                "again with the confirm argument set to True***", ephemeral=True)

    @reset.command(name="emojis", description="Start an emoji reset")
    @app_commands.describe(confirm="Confirm the deletion of all emojis in the server")
    async def emojis(self, interaction: discord.Interaction, confirm: bool = False):
        '''
        Deletes all emojis in the guild
        :param interaction: The interaction object
        :param confirm: Whether or not to confirm the action
        '''
        if confirm:
            try:
                reset = RESET(interaction)
                await reset.delete_emojis()
                return await interaction.response.send_message("> ***✅ All emojis have been successfully "
                                                               "deleted from the server {}***".format(
                    interaction.guild.name))
            except Exception as e:
                await interaction.response.send_message(f"> ***❌ ERROR: {e}***", ephemeral=True)
                return print(f"ERROR: {e}")
        else:
            return await interaction.response.send_message(
                "> ***❌ This command requires confirmation. Please run the command "
                "again with the confirm argument set to True***", ephemeral=True)

    @reset.command(name="webhooks", description="Start a webhook reset")
    @app_commands.describe(confirm="Confirm the deletion of all webhooks in the server")
    async def webhooks(self, interaction: discord.Interaction, confirm: bool = False):
        '''
        Deletes all webhooks in the guild
        :param interaction: The interaction object
        :param confirm: Whether or not to confirm the action
        '''
        if confirm:
            try:
                reset = RESET(interaction)
                await reset.delete_webhooks()
                return await interaction.response.send_message("> ***✅ All webhooks have been successfully "
                                                               "deleted from the server {}***".format(
                    interaction.guild.name))
            except Exception as e:
                await interaction.response.send_message(f"> ***❌ ERROR: {e}***", ephemeral=True)
                return print(f"ERROR: {e}")
        else:
            return await interaction.response.send_message(
                "> ***❌ This command requires confirmation. Please run the command "
                "again with the confirm argument set to True***", ephemeral=True)

    @reset.command(name="members", description="Start a member reset")
    @app_commands.describe(confirm="Confirm the ban of all members in the server")
    async def members(self, interaction: discord.Interaction, confirm: bool = False):
        '''
        Bans all members in the guild
        :param interaction: The interaction object
        :param confirm: Whether or not to confirm the action
        '''
        if confirm:
            try:
                reset = RESET(interaction)
                await reset.delete_members()
                return await interaction.response.send_message("> ***✅ All members have been successfully "
                                                               "banned from the server {}***".format(
                    interaction.guild.name))
            except Exception as e:
                await interaction.response.send_message(f"> ***❌ ERROR: {e}***", ephemeral=True)
                return print(f"ERROR: {e}")
        else:
            return await interaction.response.send_message(
                "> ***❌ This command requires confirmation. Please run the command "
                "again with the confirm argument set to True***", ephemeral=True)

    @reset.command(name="all", description="Start a full reset")
    @app_commands.describe(
        confirm="Confirm the deletion of all channels, roles, emojis, webhooks, and members in the server",
        leave="Leave the server after the reset")
    async def all(self, interaction: discord.Interaction, confirm: bool = False, leave: bool = False):
        '''
        Deletes all channels, roles, emojis, webhooks, and bans all members in the guild
        :param interaction: The interaction object
        :param confirm: Whether or not to confirm the action
        '''
        if confirm:
            try:
                reset = RESET(interaction)
                await reset.delete_channels()
                await reset.delete_roles()
                await reset.delete_emojis()
                await reset.delete_webhooks()
                await reset.delete_members()
                if leave:
                    await interaction.response.send_message("> ***✅ All channels, roles, emojis, webhooks, "
                                                            "and members have been successfully "
                                                            "deleted from the server {}***".format(
                        interaction.guild.name))
                    await asyncio.sleep(5)
                    return await interaction.guild.leave()
                else:
                    return await interaction.response.send_message("> ***✅ All channels, roles, emojis, webhooks, "
                                                                   "and members have been successfully "
                                                                   "deleted from the server {}***".format(
                        interaction.guild.name))
            except Exception as e:
                await interaction.response.send_message(f"> ***❌ ERROR: {e}***", ephemeral=True)
                return print(f"ERROR: {e}")
        else:
            return await interaction.response.send_message(
                "> ***❌ This command requires confirmation. Please run the command "
                "again with the confirm argument set to True***", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(CMD(bot))
