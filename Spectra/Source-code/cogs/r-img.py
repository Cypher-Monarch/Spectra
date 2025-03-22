# Modules we are going to require for the r-img command
import asyncpraw  # Python Reddit API Wrapper
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
import random

# Definition of a class named Rimg
class Rimg(commands.Cog):  # Links the command file to the command handler
    def __init__(self, bot):  # Initializes the bot to itself
        self.bot = bot

        # Set up Reddit API credentials
        load_dotenv()
        client_id = os.getenv("REDDIT_KEY")
        client_secret = os.getenv("REDDIT_SECRET")
        self.reddit = asyncpraw.Reddit(
            client_id=f"{client_id}", #Client id for Reddit API
            client_secret=f"{client_secret}", #Client secret for Reddit API
            user_agent="Spectra Bot (by u/Tiny_Volume4503)" #Optional part of replacing with Reddit Username
        )

    @commands.Cog.listener()  # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):  # This one is just for confirming that the command has been loaded
        print('r-img loaded')

    @app_commands.command(name="r-img", description="Sends random Reddit pictures (Top 50) from r/LandscapePhotography subreddit!")
    async def r_img(self, interaction: discord.Interaction):
        try:
            # Fetch subreddit posts
            subreddit = await self.reddit.subreddit("LandscapePhotography")
            posts = [post async for post in subreddit.hot(limit=50)]  # Fetch top 50 hot posts asynchronously

            # Choose a random post
            random_post = random.choice(posts)

            # Extract necessary fields
            Title = random_post.title
            Url = random_post.url
            Post_Url = random_post.shortlink

            # Create and send the embed
            r_image = discord.Embed(
                title=Title,
                url=Post_Url,
                color=discord.Color.orange()
            )
            r_image.set_image(url=Url)
            await interaction.response.send_message(embed=r_image)
        except Exception as e:
            # Handle errors
            await interaction.response.send_message(
                f"Failed to fetch posts from Reddit. Error: {str(e)}",
                ephemeral=True #Shows in form of error / dismissable message
            )
            print(f"Error: {str(e)}")

async def setup(bot):  # Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Rimg(bot))
