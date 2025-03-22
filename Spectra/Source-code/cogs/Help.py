#The modules we are going to require for the help command
import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog): #Links the command file to the command handler
    def __init__(self, bot):#initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):
        print('Help loaded') #This one is just for confirming that the command has been loaded (Prints it in terminal itself)

    @app_commands.command(name = "help", description = "Sends the list of all commands") #The bot is initialised to command /help
    async def help(self, interaction: discord.Interaction): #The parameters are basically the bot initialisation and the location of interaction with the bot
        Commands = """
`/calc`: Calculator on discord!!
`/cf`: Sends random chemical formula!!
`/cypher`: Encodes your message into a super secret code!!
`/decypher`: Decodes your message using a super secret code!!
`/color`: Sends random color in hex or rgb format!!
`/everything`: A little bit of everything in one command!!
`/food`: Generate a random food item based on a nutrient you want!!
`/img`: Random image based on number input!!
`/info`: Know about the Developers and Version of the bot!!
`/iss`: Sends the geological location of the ISS!!
`/music`: Sends random music genre!!
`/nasa`: Sends NASA's Picture of the Day!!
`/password`: Generate random password!!
`/ping`: Sends the time it takes your message to reach spectra!
`/quote`: Sends a random quote!!
`/rev`: Reverses a user given string!!
`/r-img`: Sends random Reddit pictures from r/landscapes subreddit!!
`/s-info`: Provides information of the server!!
`/tv`: Random TV series!!
`/wiki`: Sends random wiki article!!
"""

        embed = discord.Embed(
                title = "Sure, here is a list of all the commands",
                description = f"{Commands}",
                color = discord.Color(0xA76BCF)
            ) #Created an embedded message
        await interaction.response.send_message(embed = embed) #Sends the variable "embed" in an embedded message

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Help(bot))