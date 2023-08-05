# src/video.py
import requests

class Video:
    def __init__(self, video_id, title=None, url=None, view_count=None, like_count=None):
        self.video_id = video_id
        self.title = title
        self.url = url
        self.view_count = view_count
        self.like_count = like_count

        try:
            response = requests.get(f'https://api.example.com/videos/{video_id}')
            data = response.json()
            self.title = data.get('title')
            self.url = data.get('url')
            self.view_count = data.get('view_count')
            self.like_count = data.get('like_count')
        except requests.exceptions.RequestException:
            print(f"Error: Unable to fetch data for video with id {video_id}")

    def __str__(self):
        return self.title

    def __add__(self, other):
        if isinstance(other, Video):
            return self.view_count + other.view_count
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Video' and '{}'".format(type(other).__name__))

class PLVideo(Video):
    def __init__(self, video_id, playlist_id, title=None, url=None, view_count=None, like_count=None):
        super().__init__(video_id, title, url, view_count, like_count)
        self.playlist_id = playlist_id
