import responses
import dbmanager
import thugginbot

CurentWords= {"lovers":1, "aarg":1,"fur":1,"margs":1,"patg":1,"prom":1,"shopping":1,"spoon":1,"after":1,"arriba":1,"behold":1,"gac":1,"brothers":1,"girlypop":1,"goyank":1,"hbd":1,"mykid":1,"napscanthang":1,"rizz":1,"spoopy":1,"teampee":1,"watg":1,"zaza":1,"drunktype":1,"fortnite":1,"fuckit":1,"gobills":1,"hottub":1,"juice":1,"naked":1,"operator":1,"showerbeer":1,"souptime":1,"egg":1,"hatg":1,"chef":1,"blue":1,"munch":1,"thief":1,"besties":1,"hotsauce":1,"caillou":1,"sleepy":1,"sus":1,"fearless":1,"eep":1,"ready":1,"farmer":1,"palmtree":1,"eatg":1,"teli":1}

#Gifs are not implemnted yet this is just a place holder
CurrentGifs={"drop":"https://imgur.com/a/HWIOTwz","deck":"https://imgur.com/vjb9mxE","twerk":"https://imgur.com/l0kFAUA"}


async def process_msg(msg):
    # Get message text
    text = msg.content.lower()
    
    
    length=len(text)  
    # --== ThugginBot Commands ==--
    if text[0]=='!' and   text[1:length] in CurentWords.keys():
        text=text[1:length]
        await thugginbot.checkThugginBotCommand(msg)

    #Command to send Gifs
    elif text[0]=='!' and   text[1:length] in CurrentGifs.keys():
        text=text[1:length]
        await msg.channel.send(CurrentGifs.get(text))
    # --== ThugginThursday Command ==--
    elif len(text) == 1:
       await thugginbot.handle_thugginbot_message(msg)


    # --== General Commands ==--
    elif text.startswith('!help'):
        await responses.post_help_command(msg)

        print('POST - HelpCommand')
    
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