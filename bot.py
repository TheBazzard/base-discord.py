import discord
from discord.ext import commands

TOKEN = "" # <--- Your token.

bot = commmands.Bot(command_prefix = '') # <--- Your prefix.
bot.remove_command("help")

@bot.event                                    
async def on_ready():                                
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"")) # Import your status in "" 
    print('Bot is running.') # Message if bot start his work.

bot.run(TOKEN) 

# Be aware that this is the simplest base for a discord bot.
