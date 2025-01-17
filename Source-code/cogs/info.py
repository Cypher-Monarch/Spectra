# Modules we are going to require for the info command
import discord
from discord.ext import commands 
from discord import app_commands 

# Definition of a class named info
class Info(commands.Cog):  # Links the command file to the command handler
    def __init__(self, bot):  # Initializes the bot to itself
        self.bot = bot

    @commands.Cog.listener()  # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):  # This one is just for confirming that the command has been loaded
        print('DEV info loaded')  
    
    @app_commands.command(name="info", description="Know about the Developers and Version of the bot!!")  # The bot is initialized to command /info
    async def info(self, interaction: discord.Interaction):  # Parameters include the interaction context
       #Contains all the dev info
        devinfo = {
        "Developers": "Prattyush and Rishabh",
        "Project for": "CS Finals",
        "Last updated on": "13-10-2024",
        "Latest Version": "R2.B3.P1.G0"
        }
       #Iteratively accesses and formats the keys (titles) and values (The descriptions) of the dictionary
        result = "\n".join(f"`{key}`: {value}" for key, value in devinfo.items())
       # Create an embed for the dev info response
        embed = discord.Embed(
            title="Sure here is the dev info!!",  # Title of the embed
            description=f"{result}",  # Description containing all relevant info
            color=discord.Color.red()  # Color of the embed
        )

        # Sends the embed response to the interaction
        await interaction.response.send_message(embed=embed)

async def setup(bot):  # Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Info(bot))
