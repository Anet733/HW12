import json
import logging
from json import JSONDecodeError

logging.basicConfig(filename='basic.log')


class PostHandler:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
        posts = []
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts = json.load(file)
        except JSONDecodeError:
            logging.exception('Файл не удается преобразовать')
            return 'Файл не удается преобразовать'

        return posts

    def search_posts(self, search):
        posts = []
        for post in self.load_posts():
            if search.lower() in post['content'].lower():
                posts.append(post)
        return posts

    def add_post(self, post):
        posts = self.load_posts()
        posts.append(post)
        self.save_post_to_json(posts)

    def save_post_to_json(self, posts):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

    def load_all_posts(self):
        pass
