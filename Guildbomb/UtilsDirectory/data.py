from discord.ext import commands, tasks
import discord
import asyncio
import os

########################################################################################################################
# Paste your token and a custom prefix right here:
dc_token = "X"  # DISCORD-TOKEN
dc_prefix = "!!"  # BOT-PREFIX

########################################################################################################################

greencolors = [0x4cd137, 0x44bd32, 0xA3CB38]
redcolors = [0xeb4d4b, 0xff7979, 0xee5253]
bluecolors = [0x74b9ff, 0x487eb0, 0x686de0]

timeout = 35
waitmsg = "⏳ | Please wait..."
donemsg = "✅ | **Done.**"
no_msg = "❎ | **Okay.**"
timeout_msg = "☕ | **It took you too long to answer.**"
