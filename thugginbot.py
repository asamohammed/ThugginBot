from dbmanager import check_fetch_thugginbot_word

# check for 3 consequitigve before sending the word.
# People mess up the thugginword so thould be pluggin in hard code

async def handle_thugginbot_message(msg):
    message_history_limit = 5

    current_word = ''
    current_word_print_list = []

    async for message in msg.channel.history(limit=message_history_limit):
        text = message.content
        
        if len(text) == 1 and text.isalpha():
            text = text.upper()
            current_word = text + current_word
            current_word_print_list.append(current_word)

            fetched_row = await check_fetch_thugginbot_word(current_word)

            if len(fetched_row) == 1:
                spaced_current_word = current_word.replace("", " ")[1: -1]
                await msg.channel.send(spaced_current_word)

        else:
            # Adding them to a list, so you don't get spammed when words are sent
            current_word = current_word_print_list[-1]
            print(current_word)
            
            # Clear current word and the print list
            current_word = ''
            current_word_print_list.clear()
            break


async def add_thugginbot_word()

"""
[
    <Message 
    id=1160742452739710986 
    channel=<TextChannel id=1151212102292353104 name='bot-testing' position=0 nsfw=False news=False category_id=None> type=<MessageType.default: 0> author=<Member id=262291517098426368 name='asa.22' global_name='Asa' bot=False nick='Elsa' guild=<Guild id=1098029040381739078 name='UB Club Ultimate' shard_id=0 chunked=True member_count=126>> flags=<MessageFlags value=0>>]
"""