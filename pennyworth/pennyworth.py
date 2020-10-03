import os

from discord.ext import commands
from dotenv import load_dotenv

from events.ready import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('COMMANDS_PREFIX')

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    ready_debug_msg(bot, GUILD)
    
@bot.event
async def on_member_join(member):
    new_member_welcome_dm(member, GUILD)

bot.run(TOKEN)