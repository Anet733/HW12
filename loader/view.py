from flask import Blueprint, render_template, request

from loader.utils import save_picture
from main.utils import PostHandler
import logging


# Объявляем Blueprint
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

# Запись логов в файл
logging.basicConfig(filename='basic.log', level=logging.INFO)


# Отображение страницы для добавления поста GET
@loader_blueprint.route('/post')
def create_new_post():
    return render_template('post_form.html')


# Отображение этой же страницы для добавления поста POST
# Также если поле не заполнено или загружено не изображение, то будет ошибка
@loader_blueprint.route('/post', methods=['POST'])
def add_new_post():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        return "Какое-то поле не заполнено, проверь"
    picture_path = save_picture(picture)
    if not picture_path:
        logging.info('Загружено не изображение')
        return 'Загружено не изображение'
    post_handler = PostHandler('posts.json')
    new_post = {'pic': picture_path, 'content': content}
    post_handler.add_post(new_post)

    return render_template('post_uploaded.html', content=content, picture_path=picture_path)


