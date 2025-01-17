#The modules we are going to require for string revesal
import discord
from discord.ext import commands
from discord import app_commands
#Definition of a class named Reverse
class Reverse(commands.Cog): #Links the command file to the command handler
    def __init__(self, bot): #Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener()# Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):#This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Reverse loaded')
    
    @app_commands.command(name = "rev", description = "Reverses a user given string")#The bot is initialised to command /rev
    async def rev(self, interaction: discord.Interaction, text: str): #The parameters are basically the bot initialisation and the location of interaction with the bot and the text you want to reverse
        reversed_string = text[::-1] #The actual reversing using string slicing
        await interaction.response.send_message(reversed_string)#Sends reversed string in embedded message

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Reverse(bot))