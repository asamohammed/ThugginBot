from random import randint


async def post_help_command(msg):
    message = "**--- __Commands:__ ---**\n**!like** @user.\n**!dislike** @user.\n**!sniped** @user.\n**!likeleaderboard** - See 10 most liked members.\n**!dislikeleaderboard** - See 10 most disliked members.\n**!clout** - See 10 members with the highest Clout (likes - dislikes).\n**!killsleaderboard** - See top 10 killers.\n**!snipedleaderboard** - See 10 most sniped members.\n**!help** - See all of CloutBot\'s commands."
    await msg.channel.send(message)


async def post_tomatos_command(msg):
    if not msg.mentions:
        return
        
    else:
        # Get first mention in list
        target_user = msg.mentions[0].nick
        
        # 1 in 20 chance of sending "this guy sticks" message instead
        random_num = randint(1, 20)

        if random_num == 20:
            # Send "this guy stinks"
            message = f'BOOOO!!!!! 👎👎 BOOOOOO! 🍅🍅🥫🍅🍅🍅 --> **{target_user}**'
            await msg.channel.send(message)

            message = f'BOOOOOOOOOOOOO!!!!!! THIS GUY, **{target_user}**, STINKS!!!!!!!'
            await msg.channel.send(message)

            message = f'BOOOO!!!!! 👎👎 BOOOOOO! 🍅🍅🥫🍅🍅🍅 --> **{target_user}**'
            await msg.channel.send(message)
            
        else:
            # Send normal tomato
            message = f'BOOOO!!!!! 👎👎 BOOOOOO! 🍅🍅🥫🍅🍅🍅 --> **{target_user}**'
            await msg.channel.send(message)


async def post_like_leaderboard(msg):
    pass


async def post_dislike_leaderboard(msg):
    pass


async def post_clout_leaderboard(msg):
    pass


async def post_kills_leaderboard(msg):
    pass


async def post_sniped_leaderboard(msg):
    pass


""" Clout leadeboard
import asyncio
import asyncpg
import aiohttp
import discord

# Replace with your Discord bot token
TOKEN = 'your_discord_bot_token'

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.content.startswith('!clout'):
        await send_clout_leaderboard(message.channel)

async def send_clout_leaderboard(channel):
    # Create a database connection pool
    pool = await asyncpg.create_pool(
        user='your_user',
        password='your_password',
        database='your_database',
        host='your_host'
    )

    # Fetch data from the 'dislikes' table and sort it
    async with pool.acquire() as conn:
        rows = await conn.fetch('SELECT * FROM dislikes')
        rows.sort(key=lambda row: row['likes'] - row['dislikes'], reverse=True)

    message = ""

    async with aiohttp.ClientSession() as session:
        async with session.get(groupURL) as response:
            group = await response.json()

            rowIndex = 0
            for i in range(1, 10):
                if rowIndex >= len(rows):
                    break

                found_member = False
                for member in group['response']['members']:
                    if member['user_id'] == rows[rowIndex]['id']:
                        clout = rows[rowIndex]['likes'] - rows[rowIndex]['dislikes']
                        message += f"{i}: {member['nickname']} with {clout} clout.\n"
                        found_member = True
                        break

                if not found_member:
                    i -= 1
                rowIndex += 1

            lower_row_index = len(rows) - 1
            offset = 0
            second_message_part = ""
            for i in range(1, 3):
                if lower_row_index < rowIndex:
                    break

                found_member = False
                for member in group['response']['members']:
                    if member['user_id'] == rows[lower_row_index]['id']:
                        clout = rows[lower_row_index]['likes'] - rows[lower_row_index]['dislikes']
                        second_message_part = f"{lower_row_index + offset + 1}: {member['nickname']} with {clout} clout.\n" + second_message_part
                        found_member = True
                        break

                if not found_member:
                    i -= 1
                    offset += 1
                lower_row_index -= 1

            if lower_row_index != rowIndex:
                message += "...\n"
            message += second_message_part

    # Send the message to the specified Discord channel
    await channel.send(message)

    # Close the database connection pool
    await pool.close()

# Run the Discord bot
client.run(TOKEN)
"""