# Modules we are going to require for the image command
import discord
from discord.ext import commands
from discord import app_commands

# Definition of a class named Img
class Img(commands.Cog):  # Links the command file to the command handler
    def __init__(self, bot):  # Initializes the bot to itself
        self.bot = bot

    @commands.Cog.listener()  # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):  # This one is just for confirming that the command has been loaded
        print('Image loaded')

    @app_commands.command(name="img", description="Random image based on number input")  # The bot is initialized to command /img
    async def img(self, interaction: discord.Interaction, seed: int):  # Parameters include interaction context and a seed number
        conversion = str(seed)  # Converts the seed number to a string for URL construction
        mainlink = "https://picsum.photos/500/500?random="  # Base URL for generating a random image
        finallink = mainlink + conversion  # Final link for the image using the seed
        
        # Create an embed for the image response
        embed = discord.Embed(
            title="Your image has been generated",  # Title of the embed
            description=f"The key for this image is: `{seed}`",  # Description containing the seed number
            color=discord.Color.purple()  # Color of the embed
        )
        
        embed.set_image(url=finallink)  # Sets the image URL in the embed
        embed.add_field(name="Pro-Tip!", value=f"[Click to view another image]({finallink})", inline=False)  # Adds a clickable field to view another image
        
        # Sends the embed response to the interaction
        await interaction.response.send_message(embed=embed)

async def setup(bot):  # Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Img(bot))
