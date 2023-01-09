import json
import logging
from json import JSONDecodeError

# Логи сохраняются в файл
logging.basicConfig(filename='basic.log')


# Создаем класс
class PostHandler:
    def __init__(self, path):
        """
        Инициализируем класс
        """
        self.path = path

    def load_posts(self):
        """
        Загружаем из файла все посты и делаем проверку, всё ли ок с файлом. Возвращаем посты
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts = json.load(file)
        except JSONDecodeError:
            logging.exception('Файл не удается преобразовать')
            return 'Файл не удается преобразовать'

        return posts

    def search_posts(self, search):
        """
        Ищем посты по вхождению запроса в описание поста
        """
        posts = []
        for post in self.load_posts():
            if search.lower() in post['content'].lower():
                posts.append(post)
        return posts

    def add_post(self, post):
        """
        Добавляем к списку постов новый загруженный пост
        """
        posts = self.load_posts()
        posts.append(post)
        self.save_post_to_json(posts)

    def save_post_to_json(self, posts):
        """
        Записываем обновленный список постов в файл
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

