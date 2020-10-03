import os
import discord
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')

def ready_debug_msg(bot):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print('\tMembers in the guild:')
    for member in guild.members:
        print(
            f'\t\t'
            f'{member}\n'
        )