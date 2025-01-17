#The modules we are going to require for sending the server information
import discord
from discord.ext import commands
from discord import app_commands
#Definition of a class named Sinfo
class Sinfo(commands.Cog): #Links the command file to command handler
    def __init__(self, bot): #Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):#This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Server info loaded')

    @app_commands.command(name = "s-info", description = "Provides information of the server") #The bot is initialised to command /s-info
    async def sinfo(self, interaction: discord.Interaction): #The parameters are basically the bot initialisation and the location of interaction with the bot
        guild = interaction.guild #Retrives server of interatction
        if guild is None:
            await interaction.response.send_message(f"This command can only be used in a server, not in the DMs!!",
            ephemeral = True)
        else:
            name = interaction.guild.name #Retrives server name
            server_id = guild.id #Retrives server id
            owner = guild.owner #Retrives user id of the server owner
            members = guild.member_count #Retrives server member count
            start_time = guild.created_at.strftime("%d-%m-%y") #Retrives date of creation of server

            embed = discord.Embed(
                title = "Server info",
                description = "All server info that you need",
                color = discord.Color.gold()
            )
            embed.set_thumbnail(url = guild.icon.url)
            embed.add_field(name="`Server name`: ",value = f"{name}",inline = False)
            embed.add_field(name="`Server ID`: ",value = f"{server_id}",inline = False)
            embed.add_field(name="`Server owner`: ",value = f"{owner}",inline = False)
            embed.add_field(name="`Total members in the server`: ",value = f"{members}",inline = False)
            embed.add_field(name="`Date of creation of the server`: ",value = f"{start_time}",inline = False)
            await interaction.response.send_message(embed = embed) #Sends all parameters in an embedded message

async def setup(bot): #Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Sinfo(bot))