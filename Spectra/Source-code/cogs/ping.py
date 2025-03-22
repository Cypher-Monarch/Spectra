# The modules we are going to require for the ping command
import discord
from discord.ext import commands
from discord import app_commands
# Definition of a class named ping
class ping(commands.Cog): # Links the command file to the command handler
    def __init__(self, bot): # Initializes the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self): # This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Ping loaded')


    @app_commands.command(name = "ping", description = "Sends the time it takes your message to reach spectra!") # The bot is initialized to command /ping
    async def  ping(self, interaction: discord.Interaction): #The parameters are basically the bot initialisation and the location of interaction with the bot
        latency = interaction.client.latency*1000 #The actual latency extractor
        await interaction.response.send_message(f"**Pong!** Latency: `{latency:.2f}ms`") #Sends the message

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(ping(bot))
