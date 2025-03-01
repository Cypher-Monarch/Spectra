#The modules we are going to require for the command handler
import discord
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv
#Message's intents are initialized (defining what events the bot can respond to)
intents = discord.Intents.all()  #Enables all intents
intents.message_content = True  #Allows the bot to read the content of the message
#Bot is initialized to the command with prefix [!]
bot = commands.Bot(command_prefix='!', intents=intents)
#Bot is initialized to command !sync (Required during development phase)
# @bot.command()
# async def sync(ctx: commands.Context):
#     x = await ctx.bot.tree.sync()
#     await ctx.send(f'Synced {len(x)} commands')
#Loads all the created commands ending with extension .py
async def load():
    for filename in os.listdir('./cogs'):  #Checks for file with path ./cogs
        if filename.endswith('.py'):
            #index -3 for the last ".py" of file
            await bot.load_extension(f'cogs.{filename[:-3]}')  #Loads the command files
async def cmdhandler():  #Asynchronous function called command handler is defined 
    load_dotenv()
    Bot_Token = os.getenv("DISCORD_TOKEN") #Fetches the bot token from the .env file
    await load()
    await bot.start(f"{Bot_Token}")  #Starts the bot with the token
asyncio.run(cmdhandler())  #Starts the command handler bot asynchronously