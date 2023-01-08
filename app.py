import flask


from main.view import main_blueprint
from loader.view import loader_blueprint

POST_PATH = 'posts.json'
UPLOAD_FOLDER = "uploads/images"

app = flask.Flask(__name__)


# Регистрируем Blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config['POST_PATH'] = POST_PATH

# Из этой папки с помощью функции можно загружать файлы
@app.route('/uploads/<path:path>')
def static_dir(path):
    return flask.send_from_directory('uploads', path)


app.run(debug=True)



