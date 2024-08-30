import dbmanager
import datetime
import csv
import pandas as pd

df=pd.read_csv("TimesUsed.csv")
# check for 3 consequitigve before sending the word.
# People mess up the thugginword so thould be pluggin in hard code

async def handle_thugginbot_message(msg):
    message_history_limit = 16

    current_word = ''
    # current_word_print_list = []

    async for message in msg.channel.history(limit=message_history_limit):
        text = message.content
        #only starts adding to current word on thrursday 
        today=datetime.date.today()
        dayOfWeek=today.weekday()
        #print(dayOfWeek)
        if len(text) == 1 and text.isalpha() and dayOfWeek==3 : #3 is thursday 
            text = text.upper()
            current_word = text + current_word
            print(current_word)
            # current_word_print_list.append(current_word)

            # Words can't be less that 3 char, no need to use db resources
            #only calls the db if the  word is thuggin thursday
            if current_word=='THUGGINTHURSDAY':
                await msg.channel.send("T H U G G I N T H U R S D A Y")
                
        else:
            #print("bye")
            # Adding them to a list, so you don't get spammed when words are sent
            # current_word = current_word_print_list[-1]
            # print(current_word)
            
            # Clear current word and the print list
            current_word = ''
            # current_word_print_list.clear()
            break

async def checkThugginBotCommand(msg):
    curMsg=msg.content.upper()[1:len(msg.content)]

    fetchedRow= await dbmanager.check_fetch_thugginbot_word(curMsg)
    Tempmsg=msg.content.lower()[1:len(msg.content)]
    mask = df['Word'] == Tempmsg
    result = df[df['Word'] == Tempmsg]
    temp=result['TimesUsed'].values[0]
    print(temp)
    print(Tempmsg)
    temp=temp+1
    df.loc[mask, 'TimesUsed'] = temp
    df.to_csv("TimesUsed.csv", index=False)
    if len(fetchedRow)==1:
        if fetchedRow[0]['img_url']:
            await msg.channel.send(fetchedRow[0]['img_url'])
            