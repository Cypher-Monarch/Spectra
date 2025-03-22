#Modules we are going to require to build the /Decypher command
import discord
from discord.ext import commands
from discord import app_commands

class Decypher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Decypher loaded')


    @app_commands.command(name = "decypher", description = "Decodes your message using a super secret code.")
    async def decypher(self, interaction: discord.Interaction, message: str): 
        decoding_dict = {
    'w': 'a',  'm': 'b',  'z': 'c',  'p': 'd',  'q': 'e',
    'j': 'f',  'r': 'g',  'x': 'h',  'y': 'i',  'o': 'j',
    'n': 'k',  's': 'l',  'a': 'm',  't': 'n',  'c': 'o',
    'e': 'p',  'u': 'q',  'b': 'r',  'd': 's',  'f': 't',
    'v': 'u',  'g': 'v',  'k': 'w',  'l': 'x',  'h': 'y',  'i': 'z',

    'W': 'A',  'M': 'B',  'Z': 'C',  'P': 'D',  'Q': 'E',
    'J': 'F',  'R': 'G',  'X': 'H',  'Y': 'I',  'O': 'J',
    'N': 'K',  'S': 'L',  'A': 'M',  'T': 'N',  'C': 'O',
    'E': 'P',  'U': 'Q',  'B': 'R',  'D': 'S',  'F': 'T',
    'V': 'U',  'G': 'V',  'K': 'W',  'L': 'X',  'H': 'Y',  'I': 'Z',

    '7': '0',  '3': '1',  '8': '2',  '5': '3',  '0': '4',
    '9': '5',  '1': '6',  '4': '7',  '2': '8',  '6': '9',

    '`': '!',  '~': '@',  '|': '#',  '}': '$',  '{': '%',
    ']': '^',  '[': '&',  '=': '*',  '+': '(',  '_': ')',
    ')': '-',  '(': '_',  '*': '=',  '&': '+',  '^': '[',
    '%': '{',  '$': ']',  '#': '}',  '@': '\\',  '!': '|',
    '?': ';',  '/': ':',  '.': '\'',  ',': '"',  '"': ',',
    '\'': '<',  ';': '.',  ':': '>',  '>': '/',  '<': '?',
    ',': '`',  '.': '~',

    ' ': ' '
}

        Decoded_Message = ""
        for i in message:
            if i in decoding_dict.keys():
                Decoded_Message+=decoding_dict[i]
            else:
                Decoded_Message+=i
        embed = discord.Embed(
            title = "Let's crack this code!!",
            description = f"Here is your Decoded message: ||{Decoded_Message}||",
            color = discord.Color(0x5A009D)
        )
        embed.add_field(name = "PRO TIP:",value = "Use /cypher to encode the message.", inline = False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Decypher(bot))