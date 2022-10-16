from flask import Flask, render_template, jsonify, request
from utils import get_posts_all, get_comments_by_post_id, get_comments_count, search_for_posts
from utils import get_posts_by_user, get_post_by_pk
import logging


# логгеры
logger_api = logging.getLogger('one')

# обработчик логгера
logger_handler = logging.StreamHandler()

# форматирование(Formatter)
formatter_one = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
logger_handler.setFormatter(formatter_one)

# к журналу
logger_api.addHandler(logger_handler)
# запись логов
logging.basicConfig(filename="logs/api.log", level=logging.DEBUG)

app = Flask(__name__)


# лента
@app.route('/')
def index_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


# просмотр поста
@app.route('/posts/<int:postid>')
def post_page(postid):
    comments = get_comments_by_post_id(postid)
    posts = get_posts_all()
    count_comments = get_comments_count(postid)
    return render_template('post.html', posts=posts, comments=comments, pk=postid, count_comments=count_comments)


# поиск
@app.route('Get/search/?s=')
def search_page():
    query = request.args["s"]
    found_posts = search_for_posts(query)
    count_posts = len(found_posts)
    print(found_posts)
    return render_template('search.html', count_posts=count_posts, posts=found_posts, query=query)


# вывод по пользователю
@app.route('/user/<username>')
def user_page(username):
    posts_user = get_posts_by_user(username)
    return render_template('user-feed.html', posts_user=posts_user, username=username)


@app.route('/api/posts')
def page_api_all_posts():
    posts = get_posts_all()
    logger_api.info("Запрос /api/posts")
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>')
def page_api_post_id(post_id):
    post = get_post_by_pk(post_id)
    logger_api.info(f"Запрос /api/posts/{post_id}")
    return jsonify(post)


@app.errorhandler(404)
def error_404(error_code):
    print(f'Возникла ошибка {error_code}')
    return 'Страница, которую вы искали, не существует, код ошибки - 404'


@app.errorhandler(505)
def error_505(error_code):
    print(f'Возникла ошибка {error_code}')
    return 'Страница, которую вы искали, не существует, код ошибки - 505'


if __name__ == '__main__':
    app.run(port=5001)

