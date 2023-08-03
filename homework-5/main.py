# main.py
from src.channel import Channel
from src.video import Video, PLVideo
from src.playlist import PlayList
import datetime

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    print(moscowpython)
    print(moscowpython + highload)
    print(moscowpython - highload)
    print(highload - moscowpython)
    print(moscowpython > highload)
    print(moscowpython >= highload)
    print(moscowpython < highload)
    print(moscowpython <= highload)
    print(moscowpython == highload)

    video1 = Video('AWX4JnAnjBE', 'GIL в Python: зачем он нужен и как с этим жить',
                   'https://www.youtube.com/watch?v=AWX4JnAnjBE', 10000, 500)
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC', 'MoscowPython Meetup 78 - вступление',
                     'https://www.youtube.com/watch?v=4fObz_qw9u4', 20000, 1000)

    print(video1)
    print(video2)
    print(video1 + video2)

    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    print(pl.title)
    print(pl.url)

    duration = pl.total_duration
    print(str(duration))
    print(isinstance(duration, datetime.timedelta))
    print(duration.total_seconds())

    print(pl.show_best_video())
