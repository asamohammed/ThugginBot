import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_img_url(img_path):
    """Posts a message in the bot-testing channel of the frisbee server, then gets the url of the img after it has been uploaded to discord"""

    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHANNEL_ID = os.getenv('DISCORD_CHANNEL_TESTING_ID')

    # POST request parameters
    headers = {'Authorization': f'Bot {BOT_TOKEN}',}

    files = {'file': ('ThugginBot_ImgService.png', open(img_path, 'rb')),}

    data = {'content': 'ThugginBot Img Service'}

    # Posting img in discord and getting url
    response = requests.post(
        f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages', 
        headers=headers, 
        files=files, 
        data=data)

    data = response.json()

    return data['attachments'][0]['url']

print(get_img_url('img.png'))