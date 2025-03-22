import random
import discord
from discord.ext import commands
from discord import app_commands

class Roast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Roast loaded')


    @app_commands.command(name = "roast", description = "Sends a randomly generated roast!!")
    async def roast(self, interaction: discord.Interaction): #The parameters are basically context (or the command) and length of the password (Default is 12)
        roasts = [
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "I'd agree with you, but then we’d both be wrong.",
    "You're proof that even evolution takes a break sometimes.",
    "You bring everyone so much joy... when you leave the room.",
    "Your secrets are safe with me. I never even listen when you tell me them.",
    "You're not stupid; you just have bad luck thinking.",
    "I'd explain it to you, but I left my crayons at home.",
    "You're like a software update. Whenever I see you, I think, 'Do I really need this?'",
    "Your brain has two parts: left and right. On the left, there's nothing right, and on the right, there's nothing left.",
    "You're living proof that even mistakes can be successful.",
    "You have something on your chin... no, the third one down.",
    "You're not lazy. You’re just highly motivated to do nothing.",
    "You're like a penny. Two-faced and not worth much.",
    "You're the human version of a headache.",
    "You're not slow; you just enjoy life in slow motion.",
    "You're like a pizza without toppings—completely unnecessary.",
    "You're so fake, even China refused to copy you.",
    "You're not completely useless. You can always serve as a bad example.",
    "If you were any slower, you'd be moving backward.",
    "You're like a cloud service—always down when needed the most.",
    "You're as useful as a screen door on a submarine.",
    "You're like a WiFi signal—weak and annoying.",
    "I'd agree with you, but then we'd both be making a mistake.",
    "You're the reason they put directions on shampoo bottles.",
    "You're like a broken pencil—completely pointless.",
    "You're so dense, light bends around you.",
    "You're about as reliable as a politician's promise.",
    "You're like a speed bump—just slowing everyone down.",
    "If I had a dollar for every smart thing you said, I'd be broke.",
    "You're the human equivalent of an expired coupon.",
    "You're like a car without wheels—going nowhere fast.",
    "You're so irrelevant, autocorrect doesn't even recognize your name.",
    "You're the reason they put 'Do not eat' on silica gel packets.",
    "If brains were dynamite, you wouldn’t have enough to blow your nose.",
    "You're like a pop-up ad—nobody asked for you, and you're just annoying.",
    "You're as sharp as a marble.",
    "You bring everyone so much happiness... when you stop talking.",
    "If I wanted to hear nonsense, I'd just unmute my math teacher.",
    "Your intelligence is like a broken lightbulb—dim and flickering at best.",
    "You're like an unskippable ad—painful and unnecessary.",
    "Your thoughts are like a Windows update—long, unnecessary, and nobody wants them.",
    "You're the human equivalent of a low battery notification.",
    "You're like a USB drive with 1MB storage—outdated and barely useful.",
    "If ignorance is bliss, you must be the happiest person alive.",
    "You're so slow, even a snail overtook you and wrote a book about it.",
    "You have something on your face... oh wait, that’s just your personality.",
    "If I ate alphabet cereal, I'd probably poop out a better statement than you.",
    "If you were any more in the past, you'd be a history lesson.",
    "Your brain is like a dial-up connection—takes forever to load and still doesn't work.",
    "You're like a default wallpaper—boring and easily replaced.",
    "You're the reason why warning labels exist.",
    "You're about as useful as Ctrl+Z in real life.",
    "You're the reason AI wants to replace humans.",
    "Your WiFi signal and your personality have a lot in common—weak and disconnected.",
    "If you were any more clueless, you'd be a missing person.",
    "You're like a CAPTCHA test—nobody enjoys dealing with you.",
    "You're so irrelevant that even Google couldn’t autocomplete your name.",
    "You're like a Bluetooth device—takes forever to connect and then randomly disconnects."
]

        roast = random.choice(roasts)
        embed = discord.Embed(
            title = "You really wanted to be roasted today.",
            description = f"{roast}",
            color = 0xf1c40f 
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Roast(bot))