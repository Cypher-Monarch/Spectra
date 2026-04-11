# The modules we are going to require for Random Chemical Formulae
import random
import discord
from discord.ext import commands
from discord import app_commands

chemical_formulae = (
    "H₂O", "CO₂", "NaCl", "C₆H₁₂O₆", "NH₃", "CH₄", "H₂SO₄", "C₈H₁₈",
    "C₁₂H₂₂O₁₁", "CaCO₃", "C₂H₅OH", "NaHCO₃", "HCl", "AgNO₃", "Fe₂O₃",
    "C₆H₈O₇", "KCl", "Mg(OH)₂", "C₁₀H₁₄", "H₂O₂", "N₂", "O₂", "P₄",
    "SO₂", "H₂S", "C₆H₈", "C₃H₈", "CH₃COOH", "SiO₂", "FeSO₄", "C₁₂H₁₈O",
    "C₂H₂", "C₃H₆", "C₄H₁₀", "C₆H₁₄", "C₁₄H₁₈", "K₂SO₄", "BaCl₂",
    "CuSO₄", "Na₂S", "Pb(NO₃)₂", "Ca(OH)₂", "C₆H₆", "H₃PO₄", "FeCl₃",
    "AgCl", "C₄H₈", "H₂C₂O₄", "KNO₃", "C₁₀H₁₆", "C₁₂H₂₄", "C₁₄H₃₀",
    "C₁₈H₃₈", "H₂C₆H₁₄O₆", "C₆H₁₄N₂O₂", "MgSO₄", "Ca₃(PO₄)₂",
    "NaClO", "C₈H₁₈O", "Ag₂SO₄", "Hg₂Cl₂", "Fe₃O₄", "CaC₂", "C₄H₈O",
    "K₂Cr₂O₇", "C₆H₈O₆", "C₁₈H₃₈O₁₈", "C₇H₈", "H₂C₃O₂", "H₂CO₃",
    "C₃H₃N", "C₄H₆O₂", "C₄H₈N₂", "C₄H₈O", "C₄H₉N", "C₆H₁₈N₂",
    "C₆H₉O₂", "C₇H₁₀O", "C₈H₁₄O₁", "C₁₂H₁₈O₂", "C₉H₁₂O₂",
    "C₁₁H₁₈O₂"
) # The tuple containing the chemical formulae

# Definition of a class named cf
class cf(commands.Cog):                                                               # Links the command file to the command handler
    def __init__(self, bot):# initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener()                                                          # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):
        print('Chemical formulae loaded')                                             # This one is just for confirming that the command has been loaded (Prints it in terminal itself)


    @app_commands.command(name = "cf", description = "Sends random chemical formula") # The bot is initialised to command /cf
    async def cf(self, interaction: discord.Interaction):                             # The parameters are basically the bot initialisation and the location of interaction with the bot

        randomChemicalformula = random.choice(chemical_formulae)                      # Selects a random chemical formula from above tuple
        embed = discord.Embed(
            title = "Your Chemical Formula Has Been Generated!!",
            description = f"The chemical formula is: `{randomChemicalformula}`",
            color = discord.Color.pink()
        )                                                                             # Created an embedded message
        embed.set_image(url = "https://media.discordapp.net/attachments/1273934041300602902/1295248548715298846/chemical_formulas_image.png") # The image viewed on thhe embed
        await interaction.response.send_message(embed = embed)                        # Sends the variable "embed" in an embedded message
async def setup(bot):                                                                 # Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(cf(bot))