#The modules we are going to require for the "everything" command
import discord
import random
from discord.ext import commands
from discord import app_commands
#Definition of a class named Everything
class Everything(commands.Cog): #Links the command file to the command handler
    def __init__(self, bot): #Initalises the bot to itself
        self.bot = bot

    @commands.Cog.listener() # Registers a listener for events (enables the cog to respond to Discord events)
    async def on_ready(self): #This one is just for confirming that the command has been loaded (Prints it in terminal itself)
        print('"Everything" loaded')
    #The bot is initialised to command /everything
    @app_commands.command(name = "everything", description = "A little bit of everything in one command!")
    async def everything(self, interaction: discord.Interaction): #The parameters are basically the bot initialisation and the location of interaction with the bot
        # Combined tuples of food sources, tv sreies, chemical formulae, music genre and quotes 
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
        chemical_formulas = (
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
        )
        music_genres = (
            "Pop", "Rock", "Hip Hop", "Jazz", "Classical", "Country", "R&B", "Blues", 
            "Reggae", "Electronic", "Metal", "Funk", "Soul", "Punk", "Folk", "Disco", 
            "House", "Techno", "Trance", "Dubstep", "EDM", "Alternative", "Grunge", 
            "Indie", "Gospel", "Latin", "Ska", "Salsa", "K-pop", "J-pop", "Reggaeton", 
            "Afrobeat", "Bossa Nova", "Flamenco", "Ambient", "Trap", "Dancehall", 
            "Hardcore", "Progressive Rock", "Psychedelic", "Synthwave", "New Wave", 
            "Opera", "Orchestral", "Bluegrass", "Chillout", "Drum and Bass", "Garage", 
            "Gothic Rock", "Post Rock", "Shoegaze", "Screamo", "Post-Punk", 
            "Industrial", "Neo-Soul", "Lofi", "Chiptune", "Dub", "Breakbeat", 
            "Electro", "Minimal", "Trip-Hop", "Grime", "Latin Pop", "Mambo", "Merengue", 
            "Tango", "Zouk", "Cumbia", "Bachata", "Tejano", "Mariachi", "Bollywood", 
            "Phonk", "Qawwali", "Carnatic", "Sufi", "Raï", "Fado", "Cajun", 
            "Polka", "Klezmer", "Jungle", "Hardstyle", "Glitch Hop", "Vaporwave", 
            "Synthpop", "Dream Pop", "Garage Rock", "Math Rock", "Art Rock", 
            "Krautrock", "Post Hardcore", "Black Metal", "Death Metal", "Thrash Metal", 
            "Sludge Metal", "Doom Metal", "Melodic Metal", "Nu Metal", "Progressive Metal", 
            "Avant-garde Metal", "Power Metal", "Symphonic Metal"
        )
        quotes = (
            "Life is what happens when you're busy making other plans. – John Lennon",
            "Get busy living or get busy dying. – Stephen King",
            "You only live once, but if you do it right, once is enough. – Mae West",
            "Many of life’s failures are people who did not realize how close they were to success when they gave up. – Thomas A. Edison",
            "If you want to live a happy life, tie it to a goal, not to people or things. – Albert Einstein",
            "Never let the fear of striking out keep you from playing the game. – Babe Ruth",
            "Money and success don’t change people; they merely amplify what is already there. – Will Smith",
            "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
            "Not how long, but how well you have lived is the main thing. – Seneca",
            "If life were predictable it would cease to be life, and be without flavor. – Eleanor Roosevelt",
            "The purpose of our lives is to be happy. – Dalai Lama",
            "Life is what we make it, always has been, always will be. – Grandma Moses",
            "In the end, it’s not the years in your life that count. It’s the life in your years. – Abraham Lincoln",
            "Life is either a daring adventure or nothing at all. – Helen Keller",
            "You have within you right now, everything you need to deal with whatever the world can throw at you. – Brian Tracy",
            "Believe you can and you’re halfway there. – Theodore Roosevelt",
            "The only impossible journey is the one you never begin. – Tony Robbins",
            "Go confidently in the direction of your dreams! Live the life you’ve imagined. – Henry David Thoreau",
            "The purpose of life is a life of purpose. – Robert Byrne",
            "You miss 100% of the shots you don’t take. – Wayne Gretzky",
            "Don’t count the days, make the days count. – Muhammad Ali",
            "Act as if what you do makes a difference. It does. – William James",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
            "Never bend your head. Always hold it high. Look the world straight in the eye. – Helen Keller",
            "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
            "Do not wait for leaders; do it alone, person to person. – Mother Teresa",
            "Don’t judge each day by the harvest you reap but by the seeds that you plant. – Robert Louis Stevenson",
            "It’s never too late to be what you might have been. – George Eliot",
            "Keep smiling, because life is a beautiful thing and there’s so much to smile about. – Marilyn Monroe",
            "The best way to predict the future is to invent it. – Alan Kay",
            "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
            "Life is not measured by the number of breaths we take, but by the moments that take our breath away. – Maya Angelou",
            "The biggest adventure you can take is to live the life of your dreams. – Oprah Winfrey",
            "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
            "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
            "Challenges are what make life interesting and overcoming them is what makes life meaningful. – Joshua J. Marine",
            "In the middle of every difficulty lies opportunity. – Albert Einstein",
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. – Christian D. Larson",
            "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
            "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
            "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
            "If you really look closely, most overnight successes took a long time. – Steve Jobs",
            "The way to get started is to quit talking and begin doing. – Walt Disney",
            "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
            "Success seems to be connected with action. Successful people keep moving. They make mistakes but they don’t quit. – Conrad Hilton",
            "If you are not willing to risk the usual, you will have to settle for the ordinary. – Jim Rohn",
            "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
            "I failed my way to success. – Thomas Edison",
            "I attribute my success to this: I never gave or took any excuse. – Florence Nightingale",
            "Try not to become a man of success, but rather try to become a man of value. – Albert Einstein",
            "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
            "It does not matter how slowly you go as long as you do not stop. – Confucius",
            "Failure will never overtake me if my determination to succeed is strong enough. – Og Mandino",
            "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
            "Do not wait; the time will never be ‘just right.’ Start where you stand. – Napoleon Hill",
            "Success is how high you bounce when you hit bottom. – George S. Patton",
            "Believe you can and you’re halfway there. – Theodore Roosevelt",
            "Everything you’ve ever wanted is on the other side of fear. – George Addair",
            "Don’t limit your challenges. Challenge your limits. – Unknown",
            "Success doesn’t just find you. You have to go out and get it. – Unknown",
            "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
            "The only way to do great work is to love what you do. – Steve Jobs",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
            "The secret of getting ahead is getting started. – Mark Twain",
            "If you cannot do great things, do small things in a great way. – Napoleon Hill",
            "I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. – Jimmy Dean",
            "The best revenge is massive success. – Frank Sinatra",
            "It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome. – William James",
            "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
            "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence. – Helen Keller",
            "You define your own life. Don’t let other people write your script. – Oprah Winfrey",
            "If you look at what you have in life, you’ll always have more. If you look at what you don’t have in life, you’ll never have enough. – Oprah Winfrey",
            "You miss 100% of the shots you don’t take. – Wayne Gretzky",
            "The only person you are destined to become is the person you decide to be. – Ralph Waldo Emerson",
            "Whatever you do, do it well. – Walt Disney",
            "Tough times never last, but tough people do. – Robert H. Schuller",
            "If opportunity doesn’t knock, build a door. – Milton Berle",
            "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
            "It is never too late to be what you might have been. – George Eliot",
            "Dream big and dare to fail. – Norman Vaughan",
            "What we achieve inwardly will change outer reality. – Plutarch",
            "We generate fears while we sit. We overcome them by action. – Dr. Henry Link",
            "Do what you can with all you have, wherever you are. – Theodore Roosevelt",
            "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
            "Whether you think you can or think you can’t, you’re right. – Henry Ford",
            "People who are crazy enough to think they can change the world, are the ones who do. – Rob Siltanen",
            "Don’t stop when you’re tired. Stop when you’re done. – Unknown",
            "Everything you’ve ever wanted is on the other side of fear. – George Addair",
            "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
            "Success is liking yourself, liking what you do, and liking how you do it. – Maya Angelou",
            "Success is not in what you have, but who you are. – Bo Bennett",
            "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. – Christian D. Larson",
            "Dream big and dare to fail. – Norman Vaughan"
        )
        form = random.choice(chemical_formulas)
        quote = random.choice(quotes)
        food = random.choice(food_sources) #Selects values randomly 
        tv = random.choice(tv_series)
        music = random.choice(music_genres)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        everything = discord.Embed(
            title='Everything!',
            description=f'`Food`: {food}\n`Quote`: {quote}\n`Chemical Formula`: {form}\n`TV Series`: {tv}\n`Music Genre`: {music}\n`Colour`: Visible on the Embed!',
            color=discord.Color.from_rgb(r,g,b)
        ) #creates embed
        await interaction.response.send_message(embed=everything) #Sends the variable "everything" in an embedded message

async def setup(bot):#Marks the end of the command and adds it to a folder called _pycache_
    await bot.add_cog(Everything(bot))