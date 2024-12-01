import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variables
token = os.getenv('DISCORD_TOKEN')

if token is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set.")

# Define the intents your bot will use
intents = discord.Intents.default()
intents.messages = True  # Allow the bot to read messages to respond to commands
intents.guilds = True  # Allow the bot to receive server events

# Set command prefix and initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event that runs when the bot is connected to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Basic command example
@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')

# Run the bot using the token from the environment variable
bot.run(token)