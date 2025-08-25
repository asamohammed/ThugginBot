import dbmanager
import datetime
import csv
import pandas as pd
import json
import discord
curLen=0
df=pd.read_csv("TimesUsed.csv")
# check for 3 consequitigve before sending the word.
# People mess up the thugginword so thould be pluggin in hard code
with open("paramaters.json","r") as t:
    ThugginComplete=json.load(t)
async def handle_thugginbot_message(msg):
    message_history_limit = 16
    with open("paramaters.json","r") as t:
        ThugginComplete=json.load(t)
    current_word = ''
    # current_word_print_list = []

    async for message in msg.channel.history(limit=message_history_limit):
        if not ThugginComplete["thugginInProgress"] and not ThugginComplete["thugginComplete"]:
            
            with open("paramaters.json","w") as q:
                #thugging=thugging={"thugginComplete": False,"thugginInProgress": True,"drinkWaterOdds":ThugginComplete["drinkWaterOdds"]}
                ThugginComplete["thugginComplete"] = False
                ThugginComplete["thugginInProgress"] = True
                json.dump(ThugginComplete,q)
            with open("paramaters.json","r") as t:
                ThugginComplete=json.load(t)
        myobj = datetime.datetime.now()
        #print("Current hour ", myobj.hour)
        text = message.content
        #only starts adding to current word on thrursday 
        today=datetime.date.today()
        dayOfWeek=today.weekday()
        #print(dayOfWeek)
        if len(text) == 1 and text.isalpha() and dayOfWeek==3 and not ThugginComplete["thugginComplete"]: #3 is thursday 
            text = text.upper()
            current_word = text + current_word
            #print('THUGGINTHURSDAY' in 'THUGGINTHURSDAY')
            if current_word not in 'THUGGINTHURSDAY':
                author=msg.author
                
                df=pd.read_csv('timeOut.csv')
                newPerson={'DiscordID':author}
                tdf=pd.DataFrame(newPerson,index=[0]) 
                tdf.to_csv("timeOut.csv", mode='a', index=False,header=False)
                df=pd.read_csv('timeOut.csv')
                await msg.channel.send(f"{author.mention} This isnt verry thuggin of you")
                duration = datetime.timedelta(hours=1)
                try:
                    await author.timeout(duration, reason="not Thuggin")
                except discord.errors.Forbidden as e:
                            mods=1
                current_word=''
            #print(current_word)
            # current_word_print_list.append(current_word)

            # Words can't be less that 3 char, no need to use db resources
            #only calls the db if the  word is thuggin thursday
            if current_word=='THUGGINTHURSDAY':
                if not ThugginComplete["thugginComplete"]:
                    await msg.channel.send("T H U G G I N T H U R S D A Y")
                with open("paramaters.json","w") as q:
                    ThugginComplete['thugginInProgress'] = False
                    ThugginComplete["thugginComplete"] = True
                    #thugging=thugging={"thugginComplete": True,"thugginInProgress": False,"drinkWaterOdds":ThugginComplete["drinkWaterOdds"]}
                    json.dump(ThugginComplete,q)
                with open("paramaters.json","r") as t:
                    ThugginComplete=json.load(t)
                df=pd.read_csv('timeOut.csv')
                listOfNames= df['DiscordID'].values
                with open("timeOut.csv", "w") as f:
                    f.truncate
                    writer = csv.writer(f)
                    header = ['DiscordID']
                    writer.writerow(header)
                    f.close()    
                for member in msg.guild.members:
                    if str(member) in listOfNames:
                        try: 
                            await member.edit(timed_out_until=None)
                        except discord.errors.Forbidden as e:
                            mods=1
                




                
                
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
            