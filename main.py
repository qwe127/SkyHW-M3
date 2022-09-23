import json
import logging

from flask import Flask, render_template, jsonify, redirect, request
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

POST_PATH = './data/posts.json'
COMMENTS_PATH = './data/comments.json'
BOOKMARKS_PATH = './data/bookmarks.json'

app = Flask(__name__)
logging.basicConfig(filename='./logs/api.log', level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")


@app.route('/', methods=['GET'])
def home():
    # представление для всех постов
    posts = get_posts_all(POST_PATH)
    bookmarks = get_posts_all(BOOKMARKS_PATH)
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@app.route('/posts/<post_id>', methods=['GET'])
def post(post_id):
    # представление для одного поста
    whole_post = get_post_by_pk(post_id, POST_PATH)
    comments = get_comments_by_post_id(post_id, COMMENTS_PATH)
    return render_template('post.html', whole_post=whole_post, comments=comments)


@app.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    # представление для закладок
    bookmarks = get_posts_all(BOOKMARKS_PATH)
    return render_template('bookmarks.html', bookmarks=bookmarks)


@app.route('/bookmarks/add/<post_id>', methods=['POST'])
def add_bookmark(post_id):
    # добавляет пост в Bookmarks (для дополнительного задания) по каким-то причинам функция каждый раз переписывает предыдущую закладку
    post_to_add = get_post_by_pk(post_id, POST_PATH)
    with open('./data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(post_to_add, file)
    return redirect("/", code=302)


@app.route('/search/', methods=['GET'])
def search_page():
    # представление для поиска
    search = request.args.get('s')
    posts = search_for_posts(search, POST_PATH)
    return render_template('search.html', posts=posts, query=search)


@app.route('/user-feed/<user_name>', methods=['GET'])
def user(user_name):
    # представление с выводом постов конкретного пользователя
    user_page = get_posts_by_user(user_name, POST_PATH)
    return render_template('user-feed.html', user_page=user_page, user_name=user_name)


@app.errorhandler(404)
def page_not_found(n):
    # обработчик запросов к несуществующим страницам
    return 'Error 404', 404


@app.errorhandler(500)
def page_error(n):
    # обработчик ошибок, возникших на стороне сервера
    return 'Error 500', 500


@app.route('/api/posts/', methods=['GET'])
def json_posts():
    # возвращает полный список постов в виде JSON-списка
    posts = get_posts_all(POST_PATH)
    # залогирует обращения к эндпоинтам API
    logging.info('Request')
    return jsonify(posts)


@app.route('/api/posts/<post_id>', methods=['GET'])
def json_post(post_id):
    # возвращает пост в виде JSON-списка
    whole_post = get_post_by_pk(post_id, POST_PATH)
    # залогирует обращения к эндпоинтам API
    logging.info('Request')
    return jsonify(whole_post)


if __name__ == "__main__":
    app.run(debug=True)
