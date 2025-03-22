#The modules we are going to require for the random wiki article
import discord
from discord.ext import commands
from discord import app_commands
#Definition of a class named wiki
class wiki(commands.Cog): #Links the command file to command handler
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()# Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self): #This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Wikipedia loaded')


    @app_commands.command(name = "wiki", description = "Sends random wiki article")
    async def Wiki(self, interaction: discord.Interaction): #The parameters are basically the bot initialisation, the location of interaction with the bot
        embed = discord.Embed(
            title = "Sure here is your wiki article",
            description = f"[Click Here to View](https://en.wikipedia.org/wiki/Special:Random)",
            color = discord.Color.random()
        )
        embed.set_image(url = "https://upload.wikimedia.org/wikipedia/commons/d/de/Wikipedia_Logo_1.0.png")
        await interaction.response.send_message(embed = embed) #A link that selects random wiki articles and sends it via discord

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(wiki(bot))