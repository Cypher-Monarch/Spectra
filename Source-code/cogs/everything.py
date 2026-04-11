#The modules we are going to require for the "everything" command
import discord
import random
from discord.ext import commands
from discord import app_commands

# Import tuples from pre-existing files
from cogs.tv import tv_series
from cogs.quote import quotes
from cogs.music import music_genres
from cogs.cf import chemical_formulae

#Definition of a class named Everything
class Everything(commands.Cog):                                   # Links the command file to the command handler
    def __init__(self, bot):                                      # Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener()                                      # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):                                     #This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('"Everything" loaded')
    #The bot is initialised to command /everything
    @app_commands.command(name = "everything", description = "A little bit of everything in one command!")
    async def everything(self, interaction: discord.Interaction): # The parameters are basically the bot initialisation and the location of interaction with the bot
        # Simplified tuple for food, since the main command requires options being chosen.
        food_sources = (
            "rice", "bread", "pasta", "potatoes", "corn", "oats", "bananas", "quinoa", "sweet potatoes", "apples",
            "chicken", "fish", "eggs", "lentils", "tofu", "beans", "yogurt", "nuts", "cheese", 
            "olive oil", "avocados", "butter", "seeds", "fatty fish", "dark chocolate", "coconut oil", "whole milk",
            "spinach", "broccoli", "almonds", "salmon", "lentils", "shellfish", "pumpkin seeds", 
            "carrots", "sweet potatoes", "red peppers", "mangoes", "apricots", "liver", "pumpkin",
            "whole grains", "leafy greens", "seeds", "chicken", "bananas", 
            "oranges", "strawberries", "kiwi", "bell peppers", "tomatoes", "brussels sprouts", "papaya", 
            "mushrooms", "fortified milk", "egg yolks", "fortified cereals", "tuna", "sardines", "orange juice", 
            "sunflower seeds", "spinach", "butternut squash", "kiwi", "olive oil", "peanuts", 
            "kale", "lettuce", "green beans", "parsley", "soybeans" 
        )

        #Selects values randomly
        form = random.choice(chemical_formulae)
        quote = random.choice(quotes)
        food = random.choice(food_sources)                        
        tv = random.choice(tv_series)
        music = random.choice(music_genres)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        everything = discord.Embed(
            title='Everything!',
            description=f'`Food`: {food}\n`Quote`: {quote}\n`Chemical Formula`: {form}\n`TV Series`: {tv}\n`Music Genre`: {music}\n`Colour`: Visible on the Embed! [RGB: {r},{g},{b}]',
            color=discord.Color.from_rgb(r,g,b)
        )                                                         # creates embed
        await interaction.response.send_message(embed=everything) # Sends the variable "everything" in an embedded message

async def setup(bot):                                             # Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Everything(bot))