import asyncio
import json

import nextcord
from nextcord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",
                   case_insensitive=True, intents=intents,
                   help_command=None, status=discord.Status.offline)

@bot.event
async def on_ready():
    print("BOT ONLINE: BOT \"{}\" SUCCESSFULLY STARTED".format(bot.user.name))
    await bot.tree.sync()

with open("config.json", "r") as f:
    config = json.load(f)
    if config["token"] == "":
        print("ERROR: TOKEN NOT FOUND")
        token = input("Enter the token: ")
        config["token"] = token
        with open("config.json", "w") as f:
            json.dump(config, f, indent=4)

async def main():
    async with bot:
        await bot.load_extension('Features.cmd')
        await bot.start(config["token"])

asyncio.run(main())
