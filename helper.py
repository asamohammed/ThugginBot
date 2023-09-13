import responses
import dbmanager

async def process_msg(msg):
    # Get message text
    text = msg.content.lower()

    if text.startswith('!help'):
        await responses.post_help_command(msg)

        print('POST - HelpCommand')
    

    elif text.startswith('!tomatoes '):
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send('*STOOPID, I\'M NOT GONNA LET YOU GET THE CHANCE*')
        else:
            await responses.post_tomatos_command(msg)

        print('POST - TomatoesCommand')


    elif text.startswith('!like '):
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send('*STOOPID, I\'M NOT GONNA LET YOU GET THE CHANCE*')
        elif not msg.mentions:
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')
        else:
            # Get first mention in list
            target_user = msg.mentions[0].id
            await dbmanager.add_likes(target_user, 1)

        print('ADD - Like')


    elif text.startswith('!dislike '):
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send('*STOOPID, I\'M NOT GONNA LET YOU GET THE CHANCE*')
        elif not msg.mentions:
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')
        else:
            # Get first mention in list
            target_user = msg.mentions[0].id
            await dbmanager.add_dislikes(target_user, 1)

        print('ADD - Dislike')


    elif text.startswith('!sniped '):
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send('*STOOPID, I\'M NOT GONNA LET YOU GET THE CHANCE*')
        elif not msg.mentions:
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

        print('ADD - Sniped')


    elif text.startswith('!likeleaderboard'):
        await responses.post_like_leaderboard(msg)

        print('POST - Like_leaderboard')


    elif text.startswith('!dislikeleaderboard'):
        await responses.post_dislike_leaderboard(msg)

        print('POST - Disike_leaderboard')

    
    elif text.startswith('!cloutleaderboard'):
        await responses.post_clout_leaderboard(msg)

        print('POST - Clout_leaderboard')


    elif text.startswith('!killsleaderboard'):
        await responses.post_kills_leaderboard(msg)

        print('POST - Kills_leaderboard')

    
    elif text.startswith('!snipedleaderboard'):
        await responses.post_sniped_leaderboard(msg)

        print('POST - Sniped_leaderboard')
