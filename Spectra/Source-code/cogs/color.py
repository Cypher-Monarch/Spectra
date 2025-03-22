#The modules we are going to require for Random color
import random
import discord
from discord.ext import commands
from discord import app_commands
#Definition of a class named Color
class Color(commands.Cog): #Links the command file to the command handler
    def __init__(self, bot): #Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):#This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Color loaded')


    @app_commands.command(name = "color", description = "Sends random color in hex or rgb format")#The bot is initialised to command /color
    @app_commands.describe(choices = "Choose a format") #Choices of RGB and Hex formats are provided to the user
    @app_commands.choices(choices=[
        discord.app_commands.Choice(name='Hexadecimal', value=1),
        discord.app_commands.Choice(name='RGB', value=2)
    ])
    async def color(self, interaction: discord.Interaction,choices: discord.app_commands.Choice[int]): #The parameters are basically the bot initialisation, the location of interaction with the bot and the choices
        r = random.randint(0,255)
        g = random.randint(0,255)  #Randomly selects the values of the colors from values 0 to 255
        b = random.randint(0,255)
        color_hex = f"{r:02x}{g:02x}{b:02x}" #converts the values of each color to hexadesimal(upto two places)
        color_int = (r << 16) + (g << 8) + b #Converts it back to int type for the color set later on
        if choices. value == 1:
            embed = discord.Embed(
                title = f"The colour you generated in hex is: `#{color_hex}`",
                description = "Color is visible on the embed.",
                color = color_int
                ) #Embed in hex format
        elif choices.value == 2:
            embed = discord.Embed(
                title = f"The Color you generated in RGB is: \n`Red`: {r}\n`Green`: {g}\n`Blue`:{b}",
                description = "Color is visible on the embed.",
                color = color_int
            ) #Embed in RGB format
        await interaction.response.send_message(embed = embed) #Sends the variable "embed" in an embedded message

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Color(bot))