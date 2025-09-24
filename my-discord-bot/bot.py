import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am your bot.')

# Replace 'YOUR_BOT_TOKEN' with your bot's actual token
bot.run('YOUR_BOT_TOKEN')