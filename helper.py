import responses

async def process_msg(msg):
    # Get message text
    text = msg.content.lower()

    if text.startswith('!help'):
        await responses.post_help_command(msg)
    
    elif text.startswith('!tomatoes'):
        await responses.post_tomatos_command(msg)
