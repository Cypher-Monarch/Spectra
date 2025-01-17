# Modules we are going to require for the ISS command
import requests  # Library for making HTTP requests
import discord  
from discord.ext import commands 
from discord import app_commands  

# Definition of a class named iss
class Iss(commands.Cog):  # Links the command file to the command handler
    def __init__(self, bot):  # Initializes the bot to itself
        self.bot = bot

    @commands.Cog.listener()  # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):  # This one is just for confirming that the command has been loaded
        print('ISS loaded')  

    @app_commands.command(name="iss", description="Sends the geological location of the ISS.")  # The bot is initialized to command /iss
    async def iss(self, interaction: discord.Interaction):  # Parameters include the interaction context
        api_url = "http://api.open-notify.org/iss-now.json"  # API endpoint for ISS location
        response = requests.get(api_url)  # Makes a GET request to the API
        if response.status_code == 200:  # Checks if the response status is OK (200)
            data = response.json()  # Parses the JSON response
            position = data['iss_position']  # Extracts the ISS position data
            latitude = position['latitude']  # Gets the latitude of the ISS
            longitude = position['longitude']  # Gets the longitude of the ISS
            result = f"The ISS is at: \n`Latitude`: {latitude}\n`Longitude`: {longitude}"  # Formats the result string
        else:  # If the response status is not OK
            result = f"Failed to retrieve position, `status code`: {response.status_code}"  # Error message

        # Create an embed for the ISS location response
        embed = discord.Embed(
            title="Tracking the ISS: Latest Coordinates",  # Title of the embed
            description=f"{result}",  # Description containing the location info
            color=discord.Color(0x6A0DAD)  # Color of the embed
        )
        # Sets an image for the embed
        embed.set_image(url="https://img.pikbest.com/wp/202405/nasa-spectacular-view-of-international-space-station-orbiting-planet-earth-with-s-3d-rendering_9833209.jpg!w700wp")
        # Sends the embed response to the interaction
        await interaction.response.send_message(embed=embed)

async def setup(bot):  # Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Iss(bot))
