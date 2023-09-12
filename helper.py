import responses
import dbmanager

async def process_msg(msg):
    # Get message text
    text = msg.content.lower()

    if text.startswith('!help'):
        await responses.post_help_command(msg)
    
    elif text.startswith('!tomatoes'):
        await responses.post_tomatos_command(msg)

    elif text.startswith('!like'):
        if not msg.mentions:
            return
    
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')

        else:
            # Get first mention in list
            target_user = msg.mentions[0].id
            dbmanager.add_likes(target_user, 1)

    elif text.startswith('!dislike'):
        if not msg.mentions:
            return

        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')

        else:
            # Get first mention in list
            target_user = msg.mentions[0].id
            dbmanager.add_dislikes(target_user, 1)

    elif text.startswith('!sniped'):
        if not msg.mentions:
            return

        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')

        else:
            for target_user in msg.mentions:
                dbmanager.add_sniped(target_user, 1)
                dbmanager.add_kills(msg.author.id, 1)
