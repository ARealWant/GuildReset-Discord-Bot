'  The Imports (Do not change anything right here)  '
from UtilsDirectory.data import *

'  Enable Intents due to discord making us enable intents to get the member list   '
intents = discord.Intents.all()

'  The Bot prefix and using intents.  '
bot = commands.Bot(command_prefix=dc_prefix, intents=intents)

'  The Botstart  '
@bot.event
async def on_ready():
    print(f"...time to detonate the bomb :) [3/3]")
    print(f"Servers using {bot.user.name}:",
          len(bot.guilds))
    print("\u001b[0m")
    print("\033[94m | https://github.com/ARealWant/Guildbomb | \u001b[0m")
    print("\033[94m | Use at your own risk. | \u001b[0m")
    print(f"\033[94m | Start with {dc_prefix}help | \u001b[0m\n")
    bot.loop.create_task(status_task(bot))


'  The Statustask  '
async def status_task(bot):
    while True:
        await bot.change_presence(activity=discord.Game(name="🍕 Eating pizza..."))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name="🍹 Drinking smoothies..."))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name="👋 and raiding your Discord-Server..."))
        await asyncio.sleep(15)


'  The Errorhandling  '
@bot.event
async def on_command_error(ctx, error):
    print(f"{ctx.guild.name}:  {error}")  # Consolemessage
    if isinstance(error, commands.CommandError):
        await ctx.send(f">>> **I just found an error!** (Check also your console!)\n{error}")  # Errormessage


'  Raiding Area (All Commands listed)  '
for filename in os.listdir('EntireRaid'):
    if filename.endswith('.py'):
        bot.load_extension(f'EntireRaid.{filename[:-3]}')
print("\033[91;1m... Ready! [1/3]")
for filename in os.listdir('RaidModules'):
    if filename.endswith('.py'):
        bot.load_extension(f'RaidModules.{filename[:-3]}')
print("... Ready! [2/3]")

bot.remove_command('help')
bot.run(dc_token)
