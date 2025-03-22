#MOdules we are going to require to build the /cypher command
import discord
from discord.ext import commands
from discord import app_commands

class Cypher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cypher loaded')


    @app_commands.command(name = "cypher", description = "Encodes your message into a super secret code.")
    async def cypher(self, interaction: discord.Interaction, message: str): 
        encoding_dict = {
    'a': 'w',  'b': 'm',  'c': 'z',  'd': 'p',  'e': 'q',
    'f': 'j',  'g': 'r',  'h': 'x',  'i': 'y',  'j': 'o',
    'k': 'n',  'l': 's',  'm': 'a',  'n': 't',  'o': 'c',
    'p': 'e',  'q': 'u',  'r': 'b',  's': 'd',  't': 'f',
    'u': 'v',  'v': 'g',  'w': 'k',  'x': 'l',  'y': 'h',  'z': 'i',

    'A': 'W',  'B': 'M',  'C': 'Z',  'D': 'P',  'E': 'Q',
    'F': 'J',  'G': 'R',  'H': 'X',  'I': 'Y',  'J': 'O',
    'K': 'N',  'L': 'S',  'M': 'A',  'N': 'T',  'O': 'C',
    'P': 'E',  'Q': 'U',  'R': 'B',  'S': 'D',  'T': 'F',
    'U': 'V',  'V': 'G',  'W': 'K',  'X': 'L',  'Y': 'H',  'Z': 'I',

    '0': '7',  '1': '3',  '2': '8',  '3': '5',  '4': '0',
    '5': '9',  '6': '1',  '7': '4',  '8': '2',  '9': '6',

    '!': '`',  '@': '~',  '#': '|',  '$': '}',  '%': '{',
    '^': ']',  '&': '[',  '*': '=',  '(': '+',  ')': '_',
    '-': ')',  '_': '(',  '=': '*',  '+': '&',  '[': '^',
    '{': '%',  ']': '$',  '}': '#',  '\\': '@',  '|': '!',
    ';': '?',  ':': '/',  '\'': '.', '"': ',',  ',': '"',
    '<': '\'', '.': ';',  '>': ':',  '/': '>',  '?': '<',
    '`': ',',  '~': '.',
    ' ': ' '
}
        Encoded_Message = ""
        for i in message:
            if i in encoding_dict.keys():
                Encoded_Message+=encoding_dict[i]
            else:
                Encoded_Message+=i
        embed = discord.Embed(
            title = "Ooh someone wants to play detective!!",
            description = f"Here is your encoded message: ||{Encoded_Message}||",
            color = discord.Color(0x5A009D)
        )
        embed.add_field(name = "PRO TIP:",value = "Use /decypher to decode the message.", inline = False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Cypher(bot))