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


async def UpdateCurrentWords():
    CurentWords=json.load(f)

async def process_msg(msg):
    # Get message text
    
    water=random.randint(0,100)
    if(water==13):
        await msg.channel.send('D R I N K  W A T E R')

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

        #await thugginbot.checkThugginBotCommand(msg)
        


    #Command to send Gifs
    #elif text[0]=='!' and   text[1:length] in CurrentGifs.keys():
    #    text=text[1:length]
    #    await msg.channel.send(CurrentGifs.get(text))
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
        Bannedwords=['patg','hbd','naked']
        if(Img in Bannedwords):
            while Img in Bannedwords:
                RandomWord=random.randint(0,len(Keys)-1)
                Word=Keys[RandomWord]
                Img=Word

        await msg.channel.send(CurentWords[Word])
        BotWord=''
        for letter in Word:
            BotWord=BotWord+letter.upper()
            BotWord=BotWord+' '
        await msg.channel.send(BotWord)
        Word=Word.lower()
        mask = df['Word'] == Word
        result = df[df['Word'] == Word]
        temp=result['TimesUsed'].values[0]
        temp=temp+1
        df.loc[mask, 'TimesUsed'] = temp
        df.to_csv("TimesUsed.csv", index=False)

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

        target_user = msg.mentions[0]
        print (target_user)
        df2=pd.read_csv("clout.csv")
        listOfNames= df2['Name'].values #makes a list of all names in the csv file 
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send('*STOOPID, I\'M NOT GONNA LET YOU GET THE CHANCE*')
        elif not msg.mentions:
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send("**UHH... DON\'T CARE!!!** 😡")
        else:
            if(str(target_user) in listOfNames):
                mask = df2['Name'] == str(target_user)
                result = df2[df2['Name'] == str(target_user)] #gets the row with the target user
                Likes=result['Likes'].values[0]
                Clout=result['Clout'].values[0] #gets the vlues
                Likes=Likes+1
                Clout=Clout+1
                df2.loc[mask,'Likes']=Likes
                df2.loc[mask,'Clout']=Clout #finds locaton of values and updates them
                df2.to_csv("Clout.csv", index=False) #updates csv file
            else:
                newName={'Name': str(target_user),'Likes':1,'Dislikes':0,'Clout':1}
                tdf=pd.DataFrame(newName,index=[0]) 
                tdf.to_csv("Clout.csv", mode='a', index=False,header=False) #puts new Name in csv file

        print('ADD - Like')

    elif text.startswith('!dislike '):
        target_user = msg.mentions[0]
        df2=pd.read_csv("clout.csv")
        listOfNames= df2['Name'].values #makes a list of all names in the csv file 
        if msg.author.id == msg.mentions[0].id:
            await msg.channel.send('*STOOPID, I\'M NOT GONNA LET YOU GET THE CHANCE*')
        elif not msg.mentions:
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')
            return
        else:
            # Get first mention in list
            if(str(target_user) in listOfNames):
                mask = df2['Name'] == str(target_user)
                result = df2[df2['Name'] == str(target_user)] #gets the row with the target user
                Dislikes=result['Dislikes'].values[0]
                Clout=result['Clout'].values[0] #gets the vlues
                Dislikes=Dislikes+1
                Clout=Clout-1
                df2.loc[mask,'Dislikes']=Dislikes
                df2.loc[mask,'Clout']=Clout #finds locaton of values and updates them
                df2.to_csv("Clout.csv", index=False) #updates csv file
            else:
                newName={'Name': str(target_user),'Likes':0,'Dislikes':1,'Clout':-1}
                tdf=pd.DataFrame(newName,index=[0]) 
                tdf.to_csv("Clout.csv", mode='a', index=False,header=False) #puts new Name in csv file

        print('ADD - Dislike')

    elif text.startswith('!likeleaderboard'):
        #await responses.post_like_leaderboard(msg)
        TotalLikes={}
        with open('Clout.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #csv_reader=next(csv_reader)
            for row in csv_reader:
                #print(row)
                
                Name=row['Name']
                Likes=float(row['Likes'])
                TotalLikes[Name]=Likes
                #print(TotalLikes)
                #print(temp)
                
        for member in msg.guild.members:
            if(str(member) in TotalLikes.keys()):
                if(member.nick != None):
                    TotalLikes[str(member.nick)]=TotalLikes[str(member)]
                    del TotalLikes[str(member)]
 
        keys = list(TotalLikes.keys())
        values = list(TotalLikes.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        sorted_dict=dict(reversed(list(sorted_dict.items())))
        #print(sorted_dict)
        ListOfLikes=list(sorted_dict)
        LikeLeader='-__**Like Leaderboard**__-\n'
        for x in range(0,9):
            if(x>=len(ListOfLikes)):
                break
            else:
                person=ListOfLikes[x]
                if(sorted_dict[person]==0):
                    break
                
                LikeLeader=LikeLeader+(str(x+1)+': '+person+" with "+ str(sorted_dict[person])+'\n')
        #print(ListOfLikes)
        print('POST - Like_leaderboard')
        await msg.channel.send(LikeLeader)

    elif text.startswith('!dislikeleaderboard'):
        TotalDislikes={}
        with open('Clout.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #csv_reader=next(csv_reader)
            for row in csv_reader:
                Name=row['Name']
                Dislikes=float(row['Dislikes'])

                TotalDislikes[Name]=Dislikes
        print(TotalDislikes)
        for member in msg.guild.members:
            if(str(member) in TotalDislikes.keys()):
                if(member.nick != None):
                    TotalDislikes[str(member.nick)]=TotalDislikes[str(member)]
                    del TotalDislikes[str(member)]        
        keys = list(TotalDislikes.keys())
        values = list(TotalDislikes.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        sorted_dict=dict(reversed(list(sorted_dict.items())))
        #print(sorted_dict)
        ListOfDislikes=list(sorted_dict)
        DislikeLeader='-__**Dislike Leaderboard**__-\n'
        for x in range(0,9):
            if(x>=len(ListOfDislikes)):
                break
            else:
                person=ListOfDislikes[x]
                print(person)
                if(sorted_dict[person]==0):
                    break
                DislikeLeader=DislikeLeader+(str(x+1)+': '+person+" with "+ str(sorted_dict[person])+'\n')
        #print(ListOfLikes)
        await msg.channel.send(DislikeLeader)
        print('POST - Disike_leaderboard')

    elif text.startswith('!cloutleaderboard'):
        TotalClout={}
        with open('Clout.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #csv_reader=next(csv_reader)
            for row in csv_reader:
                Name=row['Name']
                Clout=float(row['Clout'])
                
                TotalClout[Name]=Clout
        print(TotalClout)
        for member in msg.guild.members:
            if(str(member) in TotalClout.keys()):
                if(member.nick != None):
                    TotalClout[str(member.nick)]=TotalClout[str(member)]
                    del TotalClout[str(member)]    
        keys = list(TotalClout.keys())
        values = list(TotalClout.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        sorted_dict=dict(reversed(list(sorted_dict.items())))
        #print(sorted_dict)
        ListOfClout=list(sorted_dict)
        CloutLeader='-__**Clout Leaderboard**__-\n'
        for x in range(0,9):
            if(x>=len(ListOfClout)):
                break
            else:
                person=ListOfClout[x]
                CloutLeader=CloutLeader+(str(x+1)+': '+person+" with "+ str(sorted_dict[person])+'\n')
        #print(ListOfLikes)
        await msg.channel.send(CloutLeader)

        print('POST - Clout_leaderboard')




    # --== Sniped Commands ==--
    elif text.startswith('!sniped '):
        author=msg.author
        df3=pd.read_csv('snipe.csv')
        listOfNames= df3['Name'].values
        if msg.author == msg.mentions[0]:
            await msg.channel.send('Friendly Fire Warning')
            return
        elif bool(msg.mentions[0].bot):
            await msg.channel.send('**LEAVE US ALONE!!!** 😡')
            return
        elif not msg.mentions:
            await msg.channel.send("*STOoOoPID, DIDN\'T TAG \'EM*")
        else:
            if(str(author) not in listOfNames):
                newPerson={'Name': str(author),'Kills':0,'Deaths':0,'KDA':0}
                tdf=pd.DataFrame(newPerson,index=[0]) 
                tdf.to_csv("snipe.csv", mode='a', index=False,header=False)
                df3=pd.read_csv('snipe.csv')
            for target_user in msg.mentions:
                #print(target_user)
                mask = df3['Name'] == str(author)
                result = df3[df3['Name'] == str(author)] #gets the row with the target user
                Kills=result['Kills'].values[0] #gets the values
                Kills=Kills+1
                tDeaths=result['Deaths'].values[0]
                if(tDeaths==0):
                    tDeaths=1
                df3.loc[mask,'Kills']=Kills
                df3.loc[mask,'KDA']=float(Kills/tDeaths)
                df3.to_csv("snipe.csv", index=False)
                df3=pd.read_csv('snipe.csv')

                if(str(target_user) not in listOfNames):
                    print(target_user)
                    newPerson={'Name': str(target_user),'Kills':0,'Deaths':1,'KDA':0}
                    tdf=pd.DataFrame(newPerson,index=[0]) 
                    print(tdf)
                    tdf.to_csv('snipe.csv', mode='a', index=False,header=False)
                    df3=pd.read_csv('snipe.csv')
                else:
                    mask = df3['Name'] == str(target_user)
                    result = df3[df3['Name'] == str(target_user)] #gets the row with the target user
                    Deaths=result['Deaths'].values[0] #gets the values
                    Deaths=Deaths+1
                    tKills=result['Kills'].values[0]
                    df3.loc[mask,'Deaths']=Deaths
                    df3.loc[mask,'KDA']=float(tKills/Deaths)
                    df3.to_csv("snipe.csv", index=False) #updates csv file
                    df3=pd.read_csv('snipe.csv')       
            df3.to_csv("snipe.csv", index=False)

        print('ADD - Sniped')

    elif text.startswith('!killsleaderboard'):
        TotalKills={}
        with open('snipe.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #csv_reader=next(csv_reader)
            for row in csv_reader:
                Name=row['Name']
                Kills=float(row['Kills'])


                TotalKills[Name]=Kills

        for member in msg.guild.members:
            if(str(member) in TotalKills.keys()):
                if(member.nick != None):
                    TotalKills[str(member.nick)]=TotalKills[str(member)]
                    del TotalKills[str(member)]      
        keys = list(TotalKills.keys())
        values = list(TotalKills.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        sorted_dict=dict(reversed(list(sorted_dict.items())))
        #print(sorted_dict)
        ListOfKills=list(sorted_dict)
        KillLeader='-__**Kills Leaderboard**__-\n'
        for x in range(0,9):
            if(x>=len(ListOfKills)):
                break
            else:
                person=ListOfKills[x]
                if(sorted_dict[person]==0):
                    break
                KillLeader=KillLeader+(str(x+1)+': '+person+" with "+ str(sorted_dict[person])+'\n')
        #print(ListOfLikes)
        await msg.channel.send(KillLeader)


        print('POST - Kills_leaderboard')
    
    elif text.startswith('!snipedleaderboard'):
        TotalDeaths={}
        with open('snipe.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #csv_reader=next(csv_reader)
            for row in csv_reader:
                Name=row['Name']
                Deaths=float(row['Deaths'])

                TotalDeaths[Name]=Deaths

        for member in msg.guild.members:
            if(str(member) in TotalDeaths.keys()):
                if(member.nick != None):
                    TotalDeaths[str(member.nick)]=TotalDeaths[str(member)]
                    del TotalDeaths[str(member)]      
        keys = list(TotalDeaths.keys())
        values = list(TotalDeaths.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        sorted_dict=dict(reversed(list(sorted_dict.items())))
        #print(sorted_dict)
        ListOfDeaths=list(sorted_dict)
        SnipedLeader='-__**Sniped Leaderboard**__-\n'
        for x in range(0,9):
            if(x>=len(ListOfDeaths)):
                break
            else:
                person=ListOfDeaths[x]
                if(sorted_dict[person]==0):
                    break
                SnipedLeader=SnipedLeader+(str(x+1)+': '+person+" with "+ str(sorted_dict[person])+'\n')
        #print(ListOfLikes)
        await msg.channel.send(SnipedLeader)


        print('POST - Sniped_leaderboard')

    
    elif text.startswith('!kdaleaderboard'): #posts KDA leaderbaord
        TotalKDA={}
        with open('snipe.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            #csv_reader=next(csv_reader)
            for row in csv_reader:
                Name=row['Name']
                KDA=float(row['KDA'])

                TotalKDA[Name]=KDA

        for member in msg.guild.members:
            if(str(member) in TotalKDA.keys()):
                if(member.nick != None):
                    TotalKDA[str(member.nick)]=TotalKDA[str(member)]
                    del TotalKDA[str(member)]      
        keys = list(TotalKDA.keys())
        values = list(TotalKDA.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        sorted_dict=dict(reversed(list(sorted_dict.items())))
        #print(sorted_dict)
        ListOfKDA=list(sorted_dict)
        KDALeader='-__**KDA Leaderboard**__-\n'
        for x in range(0,9):
            if(x>=len(ListOfKDA)):
                break
            else:
                person=ListOfKDA[x]
                if(sorted_dict[person]==0):
                    break
                KDALeader=KDALeader+(str(x+1)+': '+person+" with "+ str(sorted_dict[person])+'\n')
        #print(ListOfLikes)
        await msg.channel.send(KDALeader)
        print('Post KDALeaderbaord')
        return 
    
    elif text.startswith('!kda'): #posts indivdual kda
        df3=pd.read_csv('snipe.csv')
        listOfNames= df3['Name'].values
        
        author =msg.author.nick
        if(author==None or str(author) not in listOfNames):
            author=msg.author
        if(str(author) not in listOfNames):
            await msg.channel.send("Try Sinping or being Sniped First")
            return
        mask = df3['Name'] == str(author)
        result = df3[df3['Name'] == str(author)] #gets the row with the target user
        KDA=result['KDA'].values[0] #gets the values
        
        await msg.channel.send(KDA)
        print('Post KDA')
        return
    
