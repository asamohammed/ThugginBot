import responses
import dbmanager
import thugginbot
import json
import datetime
import random
import csv
import pandas as pd
from collections import OrderedDict
import numpy as np

df=pd.read_csv("TimesUsed.csv")


with open("words.json","r") as f:
    CurentWords=json.load(f)
#Gifs are not implemnted yet this is just a place holder
#CurrentGifs={"drop":"https://imgur.com/a/HWIOTwz","deck":"https://imgur.com/vjb9mxE","twerk":"https://imgur.com/l0kFAUA"}

async def UpdateCurrentWords():
    CurentWords=json.load(f)

async def process_msg(msg):
    # Get message text

    text = msg.content.lower()
    
    
    length=len(text)  
    # --== ThugginBot Commands ==--
    if text[0]=='!' and   text[1:length] in CurentWords.keys():
        text=text[1:length]
        #await thugginbot.checkThugginBotCommand(msg)
        await msg.channel.send(CurentWords[text])
        BotWord=''
        for letter in text:
            UpLetter=letter.upper()
            BotWord=BotWord+UpLetter
            BotWord=BotWord+' '
        await msg.channel.send(BotWord)
        Tempmsg=msg.content.lower()[1:len(msg.content)]
        mask = df['Word'] == Tempmsg
        result = df[df['Word'] == Tempmsg]
        temp=result['TimesUsed'].values[0]
        print(temp)
        print(Tempmsg)
        temp=temp+1
        df.loc[mask, 'TimesUsed'] = temp
        df.to_csv("TimesUsed.csv", index=False)


    #Command to send Gifs
    #elif text[0]=='!' and   text[1:length] in CurrentGifs.keys():
    #    text=text[1:length]
    #    await msg.channel.send(CurrentGifs.get(text))
    # --== ThugginThursday Command ==--
    elif len(text) == 1 and datetime.date.today().weekday()==3:
       await thugginbot.handle_thugginbot_message(msg)


    # --== General Commands ==--
    elif text.startswith('!random'):
        Keys=list(CurentWords.keys())
        RandomWord=random.randint(0,len(Keys)-1)
        Word=Keys[RandomWord]
        Img=Word
        await msg.channel.send(CurentWords[Word])
        BotWord=''
        for letter in Word:
            BotWord=BotWord+letter.upper()
            BotWord=BotWord+' '
        await msg.channel.send(BotWord)

    elif text.startswith('!help'):
        await responses.post_help_command(msg)

        print('POST - HelpCommand')
    elif(text.startswith('!mostused')):

        #data=pd.read_csv("TimesUsed.csv")
        #dataDict=data.to_dict(orient='records')
        #print(dataDict)
        TimesUsedDict={}
        with open('TimesUsed.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #csv_reader=next(csv_reader)
            for row in csv_reader:
                Word=row['Word']
                TimesUsed=float(row['TimesUsed'])
                TimesUsedDict[Word]=TimesUsed
        #print(TimesUsedDict)
            
        keys = list(TimesUsedDict.keys())
        values = list(TimesUsedDict.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        sorted_dict=dict(reversed(list(sorted_dict.items())))

        ListOfWords=list(sorted_dict)
        message='**1:** ' + str(ListOfWords[0]).upper() + ' at ' + str(int(sorted_dict[ListOfWords[0]])) + '\n**2:** ' + str(ListOfWords[1]).upper() + ' at ' + str(int(sorted_dict[ListOfWords[1]])) +'\n**3:** ' + str(ListOfWords[2]).upper() + ' at ' + str(int(sorted_dict[ListOfWords[2]])) +'\n**4:** ' + str(ListOfWords[3]).upper() + ' at ' + str(int(sorted_dict[ListOfWords[3]])) +'\n**5:** ' + str(ListOfWords[4]).upper() + ' at ' + str(int(sorted_dict[ListOfWords[4]]))
        await msg.channel.send(message)
    elif text.startswith('!haze '):
        if not msg.mentions:
            pass
        else:
            await responses.post_haze_command(msg)

        print('POST - Haze')

    elif text.startswith('!love '):
        if not msg.mentions:
            pass
        else:
            await responses.post_love_command(msg)

        print('POST - Haze')

    elif text.startswith('!tomatoes '):
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send("*STOOPID, I'M NOT GONNA LET YOU GET THE CHANCE*")
        else:
            await responses.post_tomatos_command(msg)

        print('POST - TomatoesCommand')
    
    elif text.startswith('!sawthat'):
        await responses.post_sawthat(msg)

        print('POST - SawThat') 


    # --== Like/Dislike Commands ==--
    elif text.startswith('!like '):
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send('*STOOPID, I\'M NOT GONNA LET YOU GET THE CHANCE*')
        elif not msg.mentions:
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send("**UHH... DON\'T CARE!!!** 😡")
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

    elif text.startswith('!likeleaderboard'):
        await responses.post_like_leaderboard(msg)

        print('POST - Like_leaderboard')

    elif text.startswith('!dislikeleaderboard'):
        await responses.post_dislike_leaderboard(msg)

        print('POST - Disike_leaderboard')

    elif text.startswith('!cloutleaderboard'):
        await responses.post_clout_leaderboard(msg)

        print('POST - Clout_leaderboard')


    # --== Sniped Commands ==--
    elif text.startswith('!sniped '):
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send('Friendly Fire Warning')
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')
            return
        elif not msg.mentions:
            await msg.channel.send("*STOoOoPID, DIDN\'T TAG \'EM*")
        else:
            for target_user in msg.mentions:
                await dbmanager.add_sniped(target_user.id, 1)
                await dbmanager.add_kills(msg.author.id, 1)

        print('ADD - Sniped')

    elif text.startswith('!killsleaderboard'):
        await responses.post_kills_leaderboard(msg)

        print('POST - Kills_leaderboard')
    
    elif text.startswith('!snipedleaderboard'):
        await responses.post_sniped_leaderboard(msg)

        print('POST - Sniped_leaderboard')