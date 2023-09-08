import responses

async def msg_display(msg):
    # Get message text
    text = msg.content.lower()

    if text.startswith('!help'):
        responses.post_help_command(msg)


async def like_dislike(msg):
    pass


async def snipe_kill(msg):
    pass
