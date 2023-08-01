import requests
import json
from googleapiclient.discovery import build

class Channel:
    api_key = 'AIzaSyBuuxluP5Z8a_M7xb-yUKSu6cxzWKGVius'

    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.fetch_channel_info()

    def fetch_channel_info(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={Channel.api_key}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            channel_info = data['items'][0]['snippet']
            statistics = data['items'][0]['statistics']

            self.title = channel_info['title']
            self.description = channel_info['description']
            self.view_count = statistics['viewCount']
            self.subscriber_count = statistics['subscriberCount']
            self.video_count = statistics['videoCount']

            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        else:
            raise ValueError("Channel not found or API key is invalid.")

    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"View Count: {self.view_count}")
        print(f"Subscriber Count: {self.subscriber_count}")
        print(f"Video Count: {self.video_count}")
        print(f"URL: {self.url}")

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, filename):
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'view_count': self.view_count,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'url': self.url,
        }
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    moscowpython.print_info()

    service = Channel.get_service()
    print(service.channels().list(part='snippet,statistics', id=moscowpython.channel_id).execute())

    moscowpython.to_json('moscowpython.json')
