from random import randint
import dbmanager


async def post_help_command(msg):
    message = "**--- __Commands:__ ---**\n**!like** @user.\n**!dislike** @user.\n**!sniped** @user. (must have photo)\n**!likeleaderboard** - See 10 most liked members.\n**!dislikeleaderboard** - See 10 most disliked members.\n**!clout** - See 10 members with the highest Clout (likes - dislikes).\n**!killsleaderboard** - See top 10 killers.\n**!snipedleaderboard** - See 10 most sniped members.\n**!help** - See all of CloutBot\'s commands."
    await msg.channel.send(message)


async def post_tomatos_command(msg):
    if not msg.mentions:
        return
    elif bool(msg.mentions[0].bot):
        await msg.channel.send('**LEAVE US ALONE!!!** 😡')

    else:
        # Get first mention in list
        target_user = msg.mentions[0].nick
        
        # 1 in 20 chance of sending "this guy sticks" message instead
        random_num = randint(1, 20)

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


async def post_like_leaderboard(msg):

    num_users_to_show = 10
    fetched_rows = await dbmanager.fetch_all_db_data()
    
    fetched_rows.sort(key=lambda x: x['likes'], reverse=True)

    message = ''
    message += '-__**Like Leaderboard**__-\n'

    for i, row in enumerate(fetched_rows[:num_users_to_show]):  # Get the top 10 members
        for member in msg.guild.members:
            if member.id == row['user_id']:
                message += f"{i}: {member.nick} with {row['likes']}.\n"
                break

    await msg.channel.send(message)


async def post_dislike_leaderboard(msg):

    num_users_to_show = 10

    fetched_rows = await dbmanager.fetch_all_db_data()
    
    fetched_rows.sort(key=lambda x: x['dislikes'], reverse=True)

    message = ''
    message += '-__**Dislike Leaderboard**__-\n'

    for i, row in enumerate(fetched_rows[:num_users_to_show]):  # Get the top 10 members
        for member in msg.guild.members:
            if member.id == row['user_id']:
                message += f"{i}: {member.nick} with {row['dislikes']}.\n"
                break

    await msg.channel.send(message)


async def post_clout_leaderboard(msg):
    
    num_users_to_show = 10

    fetched_rows = await dbmanager.fetch_all_db_data()

    fetched_rows.sort(key=lambda row: row['likes'] - row['dislikes'], reverse=True)

    message = ''
    message += '-__**Clout Leaderboard**__-\n'

    for i, row in enumerate(fetched_rows[:num_users_to_show]):  # Get the top 10 members
        for member in msg.guild.members:
            if member.id == row['user_id']:
                clout = row['likes'] - row['dislikes']
                message += f"{i}: {member.nick} with {clout}.\n"
                break

    # second_message_part = ""

    # for member in group['response']['members']:
    #     if member['user_id'] == rows[lower_row_index]['id']:
    #         clout = rows[lower_row_index]['likes'] - rows[lower_row_index]['dislikes']
    #         second_message_part = f"{lower_row_index + offset + 1}: {member['nickname']} with {clout} clout.\n" + second_message_part
    #         found_member = True
    #         break

    #     message += "...\n"
    # message += second_message_part

    # Send the message to the specified Discord channel
    await msg.channel.send(message)


async def post_kills_leaderboard(msg):

    num_users_to_show = 10

    fetched_rows = await dbmanager.fetch_all_db_data()
    
    fetched_rows.sort(key=lambda x: x['kills'], reverse=True)

    message = ''
    message += '-__**Kills Leaderboard**__-\n'

    for i, row in enumerate(fetched_rows[:num_users_to_show]):  # Get the top 10 members
        for member in msg.guild.members:
            if member.id == row['user_id']:
                message += f"{i}: {member.nick} with {row['kills']}.\n"
                break

    await msg.channel.send(message)


async def post_sniped_leaderboard(msg):

    num_users_to_show = 10

    fetched_rows = await dbmanager.fetch_all_db_data()
    
    fetched_rows.sort(key=lambda x: x['sniped'], reverse=True)

    message = ''
    message += '-__**Sniped Leaderboard**__-\n'

    for i, row in enumerate(fetched_rows[:num_users_to_show]):  # Get the top 10 members
        for member in msg.guild.members:
            if member.id == row['user_id']:
                message += f"{i}: {member.nick} with {row['sniped']}.\n"
                break

    await msg.channel.send(message)
