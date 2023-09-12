import responses
import dbmanager

async def process_msg(msg):
    # Get message text
    text = msg.content.lower()

    if text.startswith('!help'):
        await responses.post_help_command(msg)
    

    elif text.startswith('!tomatoes '):
        await responses.post_tomatos_command(msg)


    elif text.startswith('!like '):
        if not msg.mentions:
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')
        else:
            # Get first mention in list
            target_user = msg.mentions[0].id
            await dbmanager.add_likes(target_user, 1)


    elif text.startswith('!dislike '):
        if not msg.mentions:
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')
        else:
            # Get first mention in list
            target_user = msg.mentions[0].id
            await dbmanager.add_dislikes(target_user, 1)


    elif text.startswith('!sniped '):
        if not msg.mentions:
            return
        elif not msg.attachments:
            return
        elif msg.author.id == msg.mentions[0].id:
            await msg.channel.send('Friendly Fire Warning')
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')
            return
        else:
            for target_user in msg.mentions:
                await dbmanager.add_sniped(target_user.id, 1)
                await dbmanager.add_kills(msg.author.id, 1)


    elif text.startswith('!likeleaderboard'):
        await responses.post_like_leaderboard(msg)


    elif text.startswith('!dislikeleaderboard'):
        await responses.post_dislike_leaderboard(msg)

    
    elif text.startswith('!cloutleaderboard'):
        await responses.post_clout_leaderboard(msg)


    elif text.startswith('!killsleaderboard'):
        await responses.post_kills_leaderboard(msg)

    
    elif text.startswith('!snipedleaderboard'):
        await responses.post_sniped_leaderboard(msg)
