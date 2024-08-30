import discord
import os
import helper
from keep_alive import keep_alive
from dotenv import load_dotenv


load_dotenv()

# Initalize bot
intents = discord.Intents.all() # discord.Intents.all()
intents.messages = True
bot = discord.Client(intents = intents)


# Bot Login Confirmation
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


# Message Handling
@bot.event
async def on_message(msg):

    # TODO: check for the thursday thugginmessage not sent

    # Ignore Bot messages 
    if msg.author == bot.user:
        return
    
    # Process main chat
    elif msg.channel.name in ('all-club-chat', 'bot-testing') :
        await helper.process_msg(msg)


# Keep Bot alive by pinging flask server 
# keep_alive()

# Run bot
#bot.run(os.getenv('BOT_TOKEN'))
token = os.getenv('BOT_TOKEN')
#print(token)
bot.run(token)

