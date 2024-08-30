
import random
import dbmanager
import helper
import random


# --== General Commands ==--

async def post_help_command(msg):
    message = "**--- __Commands:__ ---**\n**!(thuginBotWord)** Send that words picture.\n**!random** Send a random thugginBot Word.\n**!sawthat** Send saw that meme.\n**!love** @user.\n**!tomatoes** @user Throw tomatoes at someone.\n**!like** @user.\n**!dislike** @user.\n**!mostused** Sends the 5 most used thugginBot Words\n**!sniped** @user. (must have photo)\n**!likeleaderboard** - See 10 most liked members.\n**!dislikeleaderboard** - See 10 most disliked members.\n**!cloutleaderboard** - See 10 members with the highest Clout (likes - dislikes).\n**!killsleaderboard** - See top 10 killers.\n**!snipedleaderboard** - See 10 most sniped members.\n**!kda** - Sends your KDA\n**!kdaleaderboard** - See 10 highest KDAs\n**!help** - See all of CloutBot\'s commands."
    await msg.channel.send(message)

async def post_tomatos_command(msg):
    if not msg.mentions:
        return
    elif bool(msg.mentions[0].bot):
        await msg.channel.send('**LEAVE US ALONE!!!** 😡')

    else:
        # Get first mention in list
        if msg.mentions[0].nick:
            target_user = msg.mentions[0].nick
        else:
            target_user = msg.mentions[0]
        
        # 1 in 20 chance of sending "this guy sticks" message instead
        random_num = random.randint(1, 20)

        # Send "this guy stinks"
        if random_num == 20:
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

async def post_sawthat(msg):
    message = 'https://cdn.discordapp.com/attachments/1151212102292353104/1160671112150134835/IMG_2100.JPG?ex=65358235&is=65230d35&hm=62829a9020e54110005b8593642263bde80732505a99aaff0e516fb1f35cd86e&'
    await msg.channel.send(message)
    

async def post_love_command(msg):
    if not msg.mentions:
        return
    elif bool(msg.mentions[0].bot):
        await msg.channel.send('**LEAVE US ALONE!!!** 😡')

    else:
        # Get first mention in list
        if msg.mentions[0].nick:
            target_user = msg.mentions[0].nick
        else:
            target_user = msg.mentions[0].display_name

        # Send love message 
        message = f'❤️❤️😻🫶🥰🥰 **{target_user}** 🥰🥰🫶😻❤️❤️'
        await msg.channel.send(message)
# --== Like/Dislike Commands ==--
async def post_like_leaderboard(msg):

    # Fetch Data
    fetched_rows = await dbmanager.fetch_all_cloutbot_data()

    # Sort Data
    fetched_rows.sort(key=lambda x: x['likes'], reverse=True)
    message = '-__**Like Leaderboard**__-\n'
    
    max_users_to_show = 10

    # Loop through the list of database records
    for row_index, row in enumerate(fetched_rows[:max_users_to_show], 1):  # Get the top 10 members
        for member in msg.guild.members:  # Loop through the server members
            if member.id == row['user_id']:
                if row['likes'] == 0:  # Don't add people with 0 likes
                    pass
                elif member.nick:  # Check if they have a server nickname
                    message += f"{row_index}: {member.nick} with {row['likes']}.\n"
                    break
                else:
                    message += f"{row_index}: {member.global_name} with {row['likes']}.\n"
                    break

    # Send message 
    await msg.channel.send(message)

async def post_dislike_leaderboard(msg):

    # Fetch Data
    fetched_rows = await dbmanager.fetch_all_cloutbot_data()

    # Sort Data
    fetched_rows.sort(key=lambda x: x['dislikes'], reverse=True)
    message = '-__**Dislike Leaderboard**__-\n'

    max_users_to_show = 10

    # Loop through the list of database records
    for row_index, row in enumerate(fetched_rows[:max_users_to_show], 1):  # Get the top 10 members
        for member in msg.guild.members:  # Loop through the server members
            if member.id == row['user_id']:
                if row['dislikes'] == 0:  # Don't add people with 0 dislikes
                    pass
                elif member.nick:  # Check if they have a server nickname
                    message += f"{row_index}: {member.nick} with {row['dislikes']}.\n"
                    break
                else:
                    message += f"{row_index}: {member.global_name} with {row['dislikes']}.\n"
                    break

    # Send message 
    await msg.channel.send(message)

async def post_clout_leaderboard(msg):

    # Fetch Data
    fetched_rows = await dbmanager.fetch_all_cloutbot_data()

    # Sort Data
    fetched_rows.sort(key=lambda row: row['likes'] - row['dislikes'], reverse=True)
    message = '-__**Clout Leaderboard**__-\n'

    max_users_to_show = 10

    # Loop through the list of database records
    for row_index, row in enumerate(fetched_rows[:max_users_to_show], 1):  # Get the top 10 members
        for member in msg.guild.members:  # Loop through the server members
            if member.id == row['user_id']:
                if (row['likes'] - row['dislikes']) == 0:  # Don't add people with 0 likes
                    pass
                elif member.nick:  # Check if they have a server nickname
                    message += f"{row_index}: {member.nick} with {row['likes'] - row['dislikes']}.\n"
                    break
                else:
                    message += f"{row_index}: {member.global_name} with {row['likes'] - row['dislikes']}.\n"
                    break

    # Send message 
    await msg.channel.send(message)


# --== Sniped Commands ==--
async def post_kills_leaderboard(msg):

    # Fetch Data
    fetched_rows = await dbmanager.fetch_all_cloutbot_data()

    # Sort Data
    fetched_rows.sort(key=lambda x: x['kills'], reverse=True)
    message = '-__**Kills Leaderboard**__-\n'

    max_users_to_show = 10

    # Loop through the list of database records
    for row_index, row in enumerate(fetched_rows[:max_users_to_show], 1):  # Get the top 10 members
        for member in msg.guild.members:  # Loop through the server members
            if member.id == row['user_id']:
                if row['kills'] == 0:  # Don't add people with 0 kills
                    pass
                elif member.nick:  # Check if they have a server nickname
                    message += f"{row_index}: {member.nick} with {row['kills']}.\n"
                    break
                else:
                    message += f"{row_index}: {member.global_name} with {row['kills']}.\n"
                    break

    # Send message 
    await msg.channel.send(message)

async def post_sniped_leaderboard(msg):

    # Fetch Data
    fetched_rows = await dbmanager.fetch_all_cloutbot_data()

    # Sort Data
    fetched_rows.sort(key=lambda x: x['sniped'], reverse=True)
    message = '-__**Sniped Leaderboard**__-\n'

    max_users_to_show = 10

    # Loop through the list of database records
    for row_index, row in enumerate(fetched_rows[:max_users_to_show], 1):  # Get the top 10 members
        for member in msg.guild.members:  # Loop through the server members
            if member.id == row['user_id']:
                if row['sniped'] == 0:  # Don't add people with 0 sniped
                    pass
                elif member.nick:  # Check if they have a server nickname
                    message += f"{row_index}: {member.nick} with {row['sniped']}.\n"
                    break
                else:
                    message += f"{row_index}: {member.global_name} with {row['sniped']}.\n"
                    break

    # Send message 
    await msg.channel.send(message)

async def post_haze_command(msg):
    if not msg.mentions:
        return
    elif bool(msg.mentions[0].bot):
        await msg.channel.send('**LEAVE US ALONE!!!** 😡')
    elif msg.author.id == msg.mentions[0].id:
        await msg.channel.send("**WHYYY?????**")
    elif not msg.author.nick=='napasaurus':
        await msg.channel.send("Presidential Power: DENIED")

    else:
        # Get first mention in list
        if msg.mentions[0].nick:
            target_user = msg.mentions[0].nick
        else:
            target_user = msg.mentions[0].display_name
    
        message = f'🥏HAAA GET HAZED **{target_user}**'
        await msg.channel.send(message)
    
