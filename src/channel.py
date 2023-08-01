import requests

class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.api_key = 'AIzaSyBuuxluP5Z8a_M7xb-yUKSu6cxzWKGVius'

        # Вызов метода для заполнения атрибутов объекта реальными данными
        self.fetch_channel_info()

    def fetch_channel_info(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.api_key}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            channel_info = data['items'][0]['snippet']
            statistics = data['items'][0]['statistics']

            self.title = channel_info['title']
            self.description = channel_info['description']
            self.url = f'https://www.youtube.com/channel/{self.channel_id}'
            self.subscriber_count = statistics['subscriberCount']
            self.video_count = statistics['videoCount']
            self.view_count = statistics['viewCount']
        else:
            raise ValueError("Channel not found or API key is invalid.")

    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"View Count: {self.view_count}")
        print(f"Subscriber Count: {self.subscriber_count}")
        print(f"Video Count: {self.video_count}")
