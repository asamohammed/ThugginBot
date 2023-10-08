import discord
import os
import helper
from keep_alive import keep_alive
from dotenv import load_dotenv

load_dotenv()

# Initalize bot
bot = discord.Client(intents = discord.Intents.all())


# Bot Login Confirmation
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


# Message Handling
@bot.event
async def on_message(msg):
    # Ignore Bot messages 
    if msg.author == bot.user:
        return
    
    # Process main chat
    elif msg.channel.name in ('all-club-chat', 'bot-testing') :
        await helper.process_msg(msg)


# Keep Bot alive by pinging flask server 
# keep_alive()

# Run bot
bot.run(os.getenv('BOT_TOKEN'))
