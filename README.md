Written by [ARealWant](https://github.com/ARealWant)
# Guildbomb - Reset your Discord server with ease!  

🗑️ Discord Bot Guildbomb will help you delete all the settings set up on your Discord server. The settings include roles, channels and e.g. server invitations. This Discord bot should help you if you are not satisfied with the current design of your server. **This bot is not intended to attack other Discord servers to cause damage, please note that this would be against the terms of use of Discord Inc.**

# Getting started
### Discord: Preparatory work
1. Open the [Discord Developer Portal](https://discord.com/developers/) and go to the [Applications Tab](https://discord.com/developers/applications).
2. Create a new application.
3. Upload the Discord bot to your server (to ensure that this bot is not used to damage larger Discord servers, the member limit is 100 members).   
3.1 You can either invite the Discord bot in the developer portal under OAuth2 > URL Generator > Bot and applications.commands > Administrator  
3.2 or by inserting the ID found at General Information into the following link: `https://discord.com/oauth2/authorize?client_id=HERE&permissions=8&scope=bot%20applications.commands`.
5. Copy the token of the application.
6. Open the bot tab and enable all Privileged Gateway Intents.
### Python: Preparatory work
1. Install Python on your [computer](https://www.python.org/downloads/) unlesss you already have it install or if you don't have a computer, on your [mobile device](https://www.python.org/community/sigs/current/mobile-sig/).
2. Download the latest .zip version from the [releases tab](https://github.com/ARealWant/Guildbomb-Discord-Bot/releases) of the repository.
3. Install Nextcord with the command
```python
# Linux/macOS
python3 -m pip install -U nextcord
```
Or if you're on windows
```python
py3 -m pip install -U nextcord
```
### Start the Discord bot
1. Start the main.py and then enter the token copied before into the terminal.
2. Type `/start` into the chat and choose one of the reset-options, please note that you have to confirm every single command.

## I would like to give this bot a try!
If you want to try this Discord bot, but don't want to reset any of your existing Discord servers, you can easily use a Discord template.  
Learn more about Discord templates by clicking [here](https://support.discord.com/hc/de/articles/360041033511-Server-Templates). Below you can see websites that provide such Discord templates.

- discordtemplates.me
- discord.style
- discords.com

## The Bot Usage:
It's important to note that these commands can **be very dangerous and should be used with caution**, as they can permanently delete important data and disrupt the functioning of a server. You should make sure to properly protect and restrict access to these commands to prevent accidental or malicious misuse.

- /start channels: Begin the process of deleting all channels on the server
- /start roles: Begin the process of deleting all roles on the server
- /start emojis: Begin the process of deleting all emojis on the server
- /start webhooks: Begin the process of deleting all webhooks on the server
- /start members: Begin the process of banning all members on the server
- /start all: Begin the process of deleting all channels, roles, emojis, webhooks, and banning all members on the server

