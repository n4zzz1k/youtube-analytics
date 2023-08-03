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
            self.view_count = int(statistics['viewCount'])
            self.subscriber_count = int(statistics['subscriberCount'])
            self.video_count = int(statistics['videoCount'])

            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        else:
            raise ValueError("Channel not found or API key is invalid.")

    def __repr__(self):
        return f"Channel('{self.title}', {self.subscriber_count})"

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count + other.subscriber_count
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Channel' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count - other.subscriber_count
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Channel' and '{}'".format(type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count == other.subscriber_count
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count < other.subscriber_count
        else:
            raise TypeError("Unsupported operand type(s) for <: 'Channel' and '{}'".format(type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count <= other.subscriber_count
        else:
            raise TypeError("Unsupported operand type(s) for <=: 'Channel' and '{}'".format(type(other).__name__))

    def __gt__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count > other.subscriber_count
        else:
            raise TypeError("Unsupported operand type(s) for >: 'Channel' and '{}'".format(type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count >= other.subscriber_count
        else:
            raise TypeError("Unsupported operand type(s) for >=: 'Channel' and '{}'".format(type(other).__name__))

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
