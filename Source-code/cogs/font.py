
'''

QUICK BREAKDOWN

1. One-liner for the dictionary-maps:
d = {}
for code in range(ord("A"), ord("Z") + 1):
    d[chr(code)] = chr(code + 0xFEE0)
2. mappings are made in dictionaries, where unicode is conveniently shifted by unicode of (original - required)
3. some mappings (such as box) support only uppercase, which is resolved by using .upper()
4. maketrans() and translate() help replace required characters.

'''

# Import modulues
import re
import discord
from discord.ext import commands
from discord import app_commands

# VAPOR (example)
VAPOR_TRANSLATION = str.maketrans({
    # Conveniently shift standard unicode to wide
    **{chr(code): chr(code + 0xFEE0) for code in range(ord("A"), ord("Z") + 1)}, # U+0041 (A) - U+FF21 (Ａ) = 0xFEE0
    **{chr(code): chr(code + 0xFEE0) for code in range(ord("a"), ord("z") + 1)}, # U+0041 (a) - U+FF21 (ａ) = 0xFEE0
    **{chr(code): chr(code + 0xFEE0) for code in range(ord("0"), ord("9") + 1)}, # U+0041 (0) - U+FF21 (０) = 0xFEE0
})
def vapor_font(text: str) -> str:
    # Replace only normal latin letters/numbers so punctuation stays readable.
    return re.sub(r"[A-Za-z0-9]+", lambda match: match.group(0).translate(VAPOR_TRANSLATION), text)

# BOX
BOX_TRANSLATION = str.maketrans({
    **{chr(code): chr(0x1F130 + (code - ord("A"))) for code in range(ord("A"), ord("Z") + 1)}
})
def box_font(text: str) -> str:
    return re.sub(r"[A-Za-z0-9]+", lambda m: m.group(0).upper().translate(BOX_TRANSLATION), text)

# FILLED BOX
BOX_FILL_TRANSLATION = str.maketrans({
    **{chr(code): chr(0x1F170 + (code - ord("A"))) for code in range(ord("A"), ord("Z") + 1)}
})
def box_fill_font(text: str) -> str:
    return re.sub(r"[A-Za-z0-9]+", lambda m: m.group(0).upper().translate(BOX_FILL_TRANSLATION), text)

# UNFORMATTED ITALIC
ITALIC_TRANSLATION = str.maketrans({
    **{chr(code): chr(0x1D608 + (code - ord("A"))) for code in range(ord("A"), ord("Z") + 1)},
    **{chr(code): chr(0x1D622 + (code - ord("a"))) for code in range(ord("a"), ord("z") + 1)},
})
def italic_font(text: str) -> str:
    return re.sub(r"[A-Za-z]+", lambda m: m.group(0).translate(ITALIC_TRANSLATION), text)

# OUTLINED
OUTLINE_TRANSLATION = str.maketrans({
    **{chr(code): chr(0x1D538 + (code - ord("A"))) for code in range(ord("A"), ord("Z") + 1)},
    **{chr(code): chr(0x1D552 + (code - ord("a"))) for code in range(ord("a"), ord("z") + 1)},
})
def outline_font(text: str) -> str:
    return re.sub(r"[A-Za-z]+", lambda m: m.group(0).translate(OUTLINE_TRANSLATION), text)

# Initialize class
class Font(commands.Cog):                                                        # Links the command file to the command handler
    def __init__(self, bot):                                                     # Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener()                                                     # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self):                                                    # This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('Font loaded')

    # Command info
    @app_commands.command(name = "font", description = "Generate your text in a fancier font!")
    @app_commands.describe(font="Choose a font!", message="Text for conversion")
    @app_commands.choices(
        font=[
            discord.app_commands.Choice(name='vapor', value=1),
            discord.app_commands.Choice(name='box', value=2),
            discord.app_commands.Choice(name='box-fill', value=3),
            discord.app_commands.Choice(name='italic', value=4),
            discord.app_commands.Choice(name='outline', value=5),

        ]
    )

    # Main function
    async def font_command(
        self,
        interaction: discord.Interaction,
        font: app_commands.Choice[int],
        message: str,
    ):
        match font.value: 
            case 1: content = vapor_font(message)
            case 2: content = box_font(message)
            case 3: content = box_fill_font(message)
            case 4: content = italic_font(message)
            case 5: content = outline_font(message)
            case _: content = message

        await interaction.response.send_message(content)

async def setup(bot):
    await bot.add_cog(Font(bot))
