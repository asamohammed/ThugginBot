import discord
import os
import helper

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
    
    # Process requests
    await helper.msg_display(msg)
    await helper.like_dislike(msg)
    await helper.snipe_kill(msg)

# Run bot
bot.run(os.getenv('BOT_TOKEN'))
