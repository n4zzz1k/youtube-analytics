# src/channel.py

import requests

class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.api_key = 'AIzaSyBuuxluP5Z8a_M7xb-yUKSu6cxzWKGVius'

    def print_info(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.api_key}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            channel_info = data['items'][0]
            title = channel_info['snippet']['title']
            description = channel_info['snippet']['description']
            view_count = channel_info['statistics']['viewCount']
            subscriber_count = channel_info['statistics']['subscriberCount']
            video_count = channel_info['statistics']['videoCount']

            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"View Count: {view_count}")
            print(f"Subscriber Count: {subscriber_count}")
            print(f"Video Count: {video_count}")
        else:
            print("Channel not found or API key is invalid.")

