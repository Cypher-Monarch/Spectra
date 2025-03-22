#The modules we are going to require for random music genre
import random
import discord
from discord.ext import commands
from discord import app_commands
#Definition of a class named music
class music(commands.Cog): #Links command file to command handler
    def __init__(self, bot): 
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self): #This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Music loaded')


    @app_commands.command(name = "music", description = "Sends random music genre") #The bot is initialised to command /music
    async def Music(self, interaction: discord.Interaction): #The parameters are basically bot initialisation and the location of interaction with the bot
        music_genres = (
    "Afrobeat", "Alternative", "Ambient", "Art Rock", "Avant-garde Metal", "Bachata", 
    "Blues", "Bluegrass", "Bollywood", "Bossa Nova", "Breakbeat", "Cajun", "Carnatic", 
    "Chillout", "Chiptune", "Classical", "Country", "Cumbia", "Dancehall", "Death Metal", 
    "Disco", "Doom Metal", "Drum and Bass", "Dub", "Dubstep", "EDM", "Electro", 
    "Electronic", "Fado", "Flamenco", "Folk", "Funk", "Garage", "Garage Rock", 
    "Gospel", "Gothic Rock", "Grime", "Grunge", "Hardcore", "Hardstyle", "Hip Hop", 
    "House", "Indie", "Industrial", "Jazz", "J-pop", "Jungle", "K-pop", "Klezmer", 
    "Krautrock", "Latin", "Latin Pop", "Lofi", "Mambo", "Mariachi", "Math Rock", 
    "Melodic Metal", "Merengue", "Metal", "Minimal", "New Wave", "Nu Metal", 
    "Opera", "Orchestral", "Phonk", "Polka", "Pop", "Post Hardcore", "Post Rock", 
    "Post-Punk", "Power Metal", "Progressive Metal", "Progressive Rock", "Psychedelic", 
    "Punk", "Qawwali", "R&B", "Raï", "Rap", "Reggae", "Reggaeton", "Rock", "Salsa", 
    "Screamo", "Shoegaze", "Ska", "Sludge Metal", "Soul", "Sufi", "Synthpop", 
    "Synthwave", "Tango", "Techno", "Tejano", "Thrash Metal", "Trance", "Trap", 
    "Trip-Hop", "Vaporwave", "World"
) #Tuple of music genre
        randomGenre = random.choice(music_genres) #Selects random music genre
        await interaction.response.send_message(f"Your random music genre is: `{randomGenre}`") #Sends the message via discord

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(music(bot))