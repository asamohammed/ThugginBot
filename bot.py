import discord
import os
import helper
from dotenv import load_dotenv

load_dotenv()

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

    # Ignore all other chats beside general
    elif not msg.channel.name == 'general':
        return
    
    
    # Process requests
    await helper.process_msg(msg)

    print(f'author {msg.author.id}')
    print(f'channel {msg.channel.id}')
    print(f'channel {msg.channel.name}')

# Run bot
bot.run(os.getenv('BOT_TOKEN'))
