#The modules we are going to require for the nasa command
import requests
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
#Definition of a class named Nasa
class Nasa(commands.Cog): #Links the command file to the command handler
    def __init__(self, bot): #Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self): #This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('NASA loaded')


    @app_commands.command(name = "nasa", description = "Sends NASA's Picture of the Day!") #The bot is initialised to command /nasa
    async def nasa(self, interaction: discord.Interaction): #The parameters are basically the bot initialisation and the location of interaction with the bot
        load_dotenv()
        api_key = os.getenv("NASA_API_KEY") #API key for the API used
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}" #URL for the api with the personal api key

        # Fetch the APOD JSON response
        response = requests.get(url)

        # Parse the JSON content into a dictionary
        content = response.json()

        # Extract the specific fields
        date = content.get('date')
        apod_url = content.get('url')
        explanation = content.get('explanation')
        title = content.get('title')

        if content.get('media_type') == "video":
            vid = content.get('url')
            watch = f"[Watch the video here]({vid})"
            NASA_embed_vid = discord.Embed(
            title=f"{title}, {date}",
            description=f"{explanation}\n{watch}",
            color=discord.Color.blurple()
            )
            await interaction.response.send_message(embed=NASA_embed_vid)

        elif content.get('media_type') == "image":
            watch = " ";
            apod_url = content.get('url')
            NASA_embed_img = discord.Embed(
            title=f"{title}, {date}",
            description=f"{explanation}\n{watch}",
            color=discord.Color.blurple()
            )
            NASA_embed_img.set_image(url=apod_url)
            await interaction.response.send_message(embed=NASA_embed_img)

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Nasa(bot))