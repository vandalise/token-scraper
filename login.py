import discord
import os
from discord.ext import commands
from colorama import Fore, Back, Style
import sys

#this is just made to show the usernames of the tokens

prefix = ","
token = sys.argv[1]

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_connect():
    print(f"{bot.user} | {token}")

bot.run(token, bot=False)