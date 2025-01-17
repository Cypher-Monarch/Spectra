#The modules we are going to require for the random password
import random
import discord
from discord.ext import commands
from discord import app_commands
#Definition of a class named Pass
class Pass(commands.Cog): #Links the command file to the command handler
    def __init__(self, bot): #Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self): #This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Password loaded')

    @app_commands.command(name = "password", description = "Generate and DMs you a randomly generated password!!") #The bot is initialised to command /password
    async def password(self, interaction: discord.Interaction, max_characters: int = 12): #The parameters are basically the bot initialisation, the location of interaction with the bot and the length of password(Default value iis 12)
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
        validCharacters = uppercase + lowercase + digits + punctuation #This is the character set for the password
        password = ""
        for i in range(max_characters):
            password += random.choice(validCharacters)
        embed = discord.Embed(
            title="Password",
            description= f"Length: `{max_characters}`",
            color=discord.Color.blue()
            )
        Password = str(password)
        password_final = f"`{Password}`"
        embed.add_field(name='Password', value=password_final, inline=False)
            
        try:
            await interaction.user.send(embed = embed)
            await interaction.response.send_message("Password sent! Check your DMs!")
        except discord.Forbidden:
            await interaction.response.send_message("I couldn't message you, please check if your DMs are unlocked.") #Sends the password in embedded message

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Pass(bot))