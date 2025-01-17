# The modules we are going to require for the calculator
import discord
from discord import app_commands
from discord.ext import commands

# Definition of a class named Calc
class Calc(commands.Cog):  # Links the command file to the command handler
    def __init__(self, bot):  # Initializes the bot to itself
        self.bot = bot

    @commands.Cog.listener()  # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):  # This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Calc loaded')

    @app_commands.command(name="calc", description="Calculator on discord!!")  # The bot is initialized to command /calc
    @app_commands.describe(operations="Choose an operator")
    @app_commands.choices(operations=[
        discord.app_commands.Choice(name='Addition', value=1),
        discord.app_commands.Choice(name='Subtraction', value=2),
        discord.app_commands.Choice(name='Multiplication', value=3),
        discord.app_commands.Choice(name='Division', value=4),
    ])
    async def calc(self, interaction: discord.Interaction, num1: int, num2: int, operations: discord.app_commands.Choice[int]):
        # Extract the operation's value
        operation = operations.value

        # Perform the appropriate operation
        if operation == 1:  # Addition
            operator = "+"
            x = num1 + num2
        elif operation == 2:  # Subtraction
            operator = "-"
            x = num1 - num2
        elif operation == 3:  # Multiplication
            operator = "*"
            x = num1 * num2
        elif operation == 4:  # Division
            if num2 == 0:  # Handling division by zero
                await interaction.response.send_message("Division by zero is not allowed!", ephemeral=True)
                return
            operator = "/"
            x = num1 / num2

        # Create an embed for the result
        embed = discord.Embed(
            title=f"The operation you chose is {operations.name}",
            description=f"The result of the calculation: \n`{num1} {operator} {num2} = {x}`",
            color=discord.Color(0x007BFF)
        )
        await interaction.response.send_message(embed=embed)  # Sends response

# Setup function to load the Cog
async def setup(bot):
    await bot.add_cog(Calc(bot))
