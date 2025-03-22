#The modules we are going to require for random tv series
import random
import discord
from discord.ext import commands
from discord import app_commands
import math
#Definition of a class named TV
class TV(commands.Cog): #Links command file to command handler
    def __init__(self, bot): #Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self): #This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('TV loaded')

    @app_commands.command(name = "tv", description = "Random TV series!")
    async def tv(self, interaction: discord.Interaction): #The parameters are basically the bot initialisation and the location of interaction with the bot
        # Combined tuple of Hollywood and Bollywood TV series
        tv_series = (
            "Breaking Bad", "Game of Thrones", "Friends", "Stranger Things", "The Office", "The Mandalorian", 
            "The Witcher", "Sherlock", "Better Call Saul", "The Crown", "Succession", "The Boys", 
            "Westworld", "House of Cards", "Money Heist", "The Big Bang Theory", "The Walking Dead", 
            "Peaky Blinders", "Black Mirror", "True Detective", "Euphoria", "Lucifer", "The Umbrella Academy", 
            "Fargo", "Ozark", "Chernobyl", "How I Met Your Mother", "Vikings", "Dexter", "Narcos", 
            "The Marvelous Mrs. Maisel", "Homeland", "Brooklyn Nine-Nine", "WandaVision", "Parks and Recreation", 
            "Sacred Games", "Mirzapur", "The Family Man", "Paatal Lok", "Made in Heaven", "Aarya", 
            "Scam 1992", "Delhi Crime", "Special Ops", "Breathe", "Inside Edge", "Asur", "Criminal Justice", 
            "TVF Pitchers", "Kota Factory", "Permanent Roommates", "Panchayat", "Aspirants", "Little Things", 
            "Bandish Bandits", "Four More Shots Please!", "Bose: Dead or Alive", "Hostages", "Rangbaaz", "Bard of Blood"
        )
        x = random.choice(tv_series) #Randomly selects a tv series
        await interaction.response.send_message(f'I choose **`{x}`**') #Sends respective tv seeries via discord

async def setup(bot):#Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(TV(bot))