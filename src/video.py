# src/video.py
class Video:
    def __init__(self, video_id, title, url, view_count, like_count):
        self.video_id = video_id
        self.title = title
        self.url = url
        self.view_count = view_count
        self.like_count = like_count

    def __str__(self):
        return self.title

    def __add__(self, other):
        if isinstance(other, Video):
            return self.view_count + other.view_count
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Video' and '{}'".format(type(other).__name__))

class PLVideo(Video):
    def __init__(self, video_id, playlist_id, title, url, view_count, like_count):
        super().__init__(video_id, title, url, view_count, like_count)
        self.playlist_id = playlist_id
