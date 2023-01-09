import flask

# Загружаем Blueprints
from main.view import main_blueprint
from loader.view import loader_blueprint

# Вот тут я что-то не совсем понимаю для чего эти 2 переменные... Что будет, если их не указать???
POST_PATH = 'posts.json'
UPLOAD_FOLDER = "uploads/images"


app = flask.Flask(__name__)


# Регистрируем Blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# И здесь мне тоже не совсем понятно, почему мы используем POST_PATH и что это в данном случае значит
app.config['POST_PATH'] = POST_PATH

# Из этой папки с помощью функции можно загружать файлы
@app.route('/uploads/<path:path>')
def static_dir(path):
    return flask.send_from_directory('uploads', path)

#Запускаем)
app.run(debug=True)

# А еще вопрос, почему после загрузки своих постов данные, которые были в posts.json отображаются как то странно?
# Вот например так: u0431ыло бы совсем неинте\. Эмм и не копируются нормально...
# Зато мои новые добавленные посты я вижу в этом файле в нормальном виде

# А также вопрос по поводу пути к файлу css в HTML файлах У меня он:../../static/style.css"
# И если я использую путь, как в разборе, то файлы его не видят. Ходя папка у меня лежит в папке проекта, а не глубже.

# Почему в main.utils мы сначала пишем функцию add_post, а только потом save_post_to_json
# Хотя в первой уже используется вторая функция. Если их поменять местами, то логика программы умирает(


