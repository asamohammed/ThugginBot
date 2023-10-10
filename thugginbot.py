from dbmanager import check_fetch_thugginbot_word

# check for 3 consequitigve before sending the word.
# People mess up the thugginword so thould be pluggin in hard code

async def handle_thugginbot_message(msg):
    message_history_limit = 20

    current_word = ''
    current_word_print_list = []

    async for message in msg.channel.history(limit=message_history_limit):
        text = message.content
        
        if len(text) == 1 and text.isalpha():
            text = text.upper()
            current_word = text + current_word
            current_word_print_list.append(current_word)

            # Words can't be less that 3 char, no need to use db resources
            if len(current_word) >= 3:
                fetched_row = await check_fetch_thugginbot_word(current_word)

                if len(fetched_row) == 1:
                    if fetched_row[0]['img_url']:
                        await msg.channel.send(fetched_row[0]['img_url'])

                    spaced_current_word = current_word.replace("", " ")[1: -1]
                    await msg.channel.send(spaced_current_word)
                    
                    break
                
        else:
            # Adding them to a list, so you don't get spammed when words are sent
            current_word = current_word_print_list[-1]
            print(current_word)
            
            # Clear current word and the print list
            current_word = ''
            current_word_print_list.clear()
            break
