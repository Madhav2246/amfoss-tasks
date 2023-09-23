import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from scraper import scrape_live_scores

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='livescore')
async def live_score(ctx):
    live_scores = scrape_live_scores()
    await ctx.send(live_scores)

@bot.command(name='generate')
async def generate_csv(ctx):
    # Add code to generate CSV here if needed
    await ctx.send('Generating CSV...')  # Placeholder message

@bot.command(name='help')
async def bot_help(ctx):
    help_message = "/livescore - Get live cricket scores\n/generate - Generate CSV file\n/help - Get a list of commands"
    await ctx.send(help_message)

bot.run(TOKEN)

