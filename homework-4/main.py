# main.py
from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем экземпляры класса Video и PLVideo
    video1 = Video('AWX4JnAnjBE', 'GIL в Python: зачем он нужен и как с этим жить', 'https://www.youtube.com/watch?v=AWX4JnAnjBE', 1000, 100)
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC', 'MoscowPython Meetup 78 - вступление', 'https://www.youtube.com/watch?v=4fObz_qw9u4', 2000, 200)

    # Используем метод __str__ для вывода названия видео
    print(str(video1))  # 'GIL в Python: зачем он нужен и как с этим жить'
    print(str(video2))  # 'MoscowPython Meetup 78 - вступление'

    # Проверяем, что класс PLVideo наследует атрибуты от Video
    print(video2.video_id)  # '4fObz_qw9u4'
    print(video2.view_count)  # 2000

    # Проверяем, что класс PLVideo имеет свой атрибут playlist_id
    print(video2.playlist_id)  # 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
