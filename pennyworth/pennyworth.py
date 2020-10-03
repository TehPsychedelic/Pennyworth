import os

from discord.ext import commands
from dotenv import load_dotenv

from events.ready import *
from events.member_join import *
from commands.reply import *

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
    await new_member_welcome_dm(member, GUILD)
    
@bot.command(name='reply')
async def on_reply_cmd(ctx, arg):
    await reply_command(ctx, arg)

bot.run(TOKEN)