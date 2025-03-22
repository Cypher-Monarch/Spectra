#Modules required for the random food items command
import random
import discord
from discord.ext import commands
from discord import app_commands

class Food(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Food loaded')

    # The bot command to select food based on nutrient and diet
    @app_commands.command(name="food", description="Generate a random food item based on a nutrient and diet!")
    @app_commands.describe(nutrient="Choose a nutrient!", diet="Choose your diet preference!")
    @app_commands.choices(
        nutrient=[
            discord.app_commands.Choice(name='Carbohydrates', value=1),
            discord.app_commands.Choice(name='Proteins', value=2),
            discord.app_commands.Choice(name='Fats', value=3),
            discord.app_commands.Choice(name='Minerals', value=4),
        ],
        diet=[
            discord.app_commands.Choice(name='Vegetarian', value=1),
            discord.app_commands.Choice(name='Non-Vegetarian', value=2),
        ]
    )
    async def food(self, interaction: discord.Interaction, nutrient: discord.app_commands.Choice[int], diet: discord.app_commands.Choice[int]):
        
        # Vegetarian and Non-Vegetarian food lists for Carbohydrates
        if nutrient.value == 1:
            if diet.value == 1:  # Vegetarian
                foods = ["Rice", "Pasta", "Bread", "Potatoes", "Quinoa", "Oats", "Barley", "Corn", "Apples", "Bananas", 
                         "Berries", "Oranges", "Pumpkin", "Spinach", "Kale", "Broccoli", "Cabbage", "Tomatoes", 
                         "Bell Peppers", "Carrots"]
            elif diet.value == 2:  # Non-Vegetarian
                foods = ["Eggs", "Milk Bread", "Bagels", "Liver Spread", "Meatloaf", "Fish Taco", "Lamb Wrap", "Chicken Wrap",
                         "Chicken Burrito", "Shrimp Stir-fry", "Salmon Poke", "Sushi", "Fish Sandwich", "Lamb Sandwich", 
                         "Steak Salad", "Tuna Wrap", "Salmon Salad", "Prawn Rice", "Shrimp Rice", "Lobster Roll"]
        
        # Vegetarian and Non-Vegetarian food lists for Proteins
        elif nutrient.value == 2:
            if diet.value == 1:  # Vegetarian
                foods = ["Tofu", "Greek Yogurt", "Cottage Cheese", "Lentils", "Chickpeas", "Quinoa", "Nuts", "Seeds", 
                         "Peanut Butter", "Almonds", "Walnuts", "Tempeh", "Edamame", "Protein Powder", "Black Beans", 
                         "Kidney Beans", "Soy Milk", "Cheese", "Hemp Seeds", "Chia Seeds"]
            elif diet.value == 2:  # Non-Vegetarian
                foods = ["Chicken Breast", "Turkey", "Fish", "Lean Beef", "Pork", "Bacon", "Duck", "Shrimp", "Mussels", 
                         "Lamb", "Crab", "Scallops", "Rabbit", "Bison", "Seitan", "Fish Roe", "Octopus", "Clams", 
                         "Crab Cakes", "Tuna"]
        
        # Vegetarian and Non-Vegetarian food lists for Fats
        elif nutrient.value == 3:
            if diet.value == 1:  # Vegetarian
                foods = ["Avocado", "Olive Oil", "Coconut Oil", "Butter", "Nuts", "Seeds", "Fatty Fish", "Cheese", 
                         "Dark Chocolate", "Egg Yolks", "Full-Fat Dairy", "Tahini", "Nut Butters", "Lard", "Ghee", 
                         "Sunflower Oil", "Canola Oil", "Safflower Oil", "Sesame Oil", "Walnut Oil"]
            elif diet.value == 2:  # Non-Vegetarian
                foods = ["Grass-Fed Beef", "Coconut Cream", "Duck Fat", "Bacon", "Lard", "Fatty Fish", "Butter", "Cheese", 
                         "Salmon", "Mackerel", "Olive Oil", "Avocado Oil", "Ghee", "Pistachios", "Macadamia Nuts", 
                         "Hazelnuts", "Poppy Seed Oil", "Camelina Oil", "Hemp Seed Oil", "Walnut Oil"]
        
        # Vegetarian and Non-Vegetarian food lists for Minerals
        elif nutrient.value == 4:
            if diet.value == 1:  # Vegetarian
                foods = ["Spinach", "Kale", "Broccoli", "Brussels Sprouts", "Sweet Potatoes", "Seaweed", "Nuts", "Seeds", 
                         "Whole Grains", "Legumes", "Chickpeas", "Quinoa", "Dark Chocolate", "Almonds", "Cashews", 
                         "Lentils", "Black Beans", "Chia Seeds", "Lentils", "Pumpkin Seeds"]
            elif diet.value == 2:  # Non-Vegetarian
                foods = ["Fish", "Shellfish", "Dairy Products", "Eggs", "Crab", "Salmon", "Shrimp", "Liver", "Oysters", 
                         "Clams", "Seaweed", "Chicken", "Pork", "Beef", "Mussels", "Mackerel", "Tuna", "Cod", "Halibut", "Tilapia"]
        
        # Send the random food suggestion
        if foods:
            selected_food = random.choice(foods)
            await interaction.response.send_message(f"Try out **`{selected_food}`**!")
        else:
            await interaction.response.send_message("Sorry, no food found for the selected options.")

async def setup(bot):
    await bot.add_cog(Food(bot))
