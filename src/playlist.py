
import requests
import datetime

class PlayList:
    api_key = 'AIzaSyBuuxluP5Z8a_M7xb-yUKSu6cxzWKGVius'

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.fetch_playlist_info()

    def fetch_playlist_info(self):
        url = f'https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={self.playlist_id}&key={PlayList.api_key}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            playlist_info = data['items'][0]['snippet']

            self.title = playlist_info['title']
            self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
            self.video_ids = self.get_video_ids()
        else:
            raise ValueError("Playlist not found or API key is invalid.")

    def get_video_ids(self):
        url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={self.playlist_id}&key={PlayList.api_key}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            return [item['contentDetails']['videoId'] for item in data['items']]
        else:
            return []

    @property
    def total_duration(self):
        total_seconds = 0
        for video_id in self.video_ids:
            duration = self.get_video_duration(video_id)
            total_seconds += duration
        return datetime.timedelta(seconds=total_seconds)

    def get_video_duration(self, video_id):
        url = f'https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={PlayList.api_key}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            duration_str = data['items'][0]['contentDetails']['duration']
            duration = self.parse_duration(duration_str)
            return duration
        else:
            return 0

    def parse_duration(self, duration_str):
        duration_str = duration_str[2:]  # Remove 'PT' at the beginning
        seconds = 0
        for part in duration_str.split('M'):
            if 'H' in part:
                hours, minutes = part.split('H')
                seconds += int(hours) * 3600
                if minutes:
                    seconds += int(minutes) * 60
            elif 'S' in part:
                seconds += int(part[:-1])
        return seconds

    def show_best_video(self):
        max_likes = -1
        best_video_url = None
        for video_id in self.video_ids:
            likes = self.get_video_likes(video_id)
            if likes > max_likes:
                max_likes = likes
                best_video_url = f"https://youtu.be/{video_id}"
        return best_video_url

    def get_video_likes(self, video_id):
        url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={PlayList.api_key}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            return int(data['items'][0]['statistics']['likeCount'])
        else:
            return 0

