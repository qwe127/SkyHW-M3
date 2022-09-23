import json


def get_posts_all(path):
    """возвращает посты"""
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_all(path):
    """возвращает комментарии"""
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_bookmarks_all(path):
    """возвращает закладки"""
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name, path):
    """возвращает посты определенного пользователя."""
    result = []
    for post in get_posts_all(path):
        if user_name.lower() in post['poster_name'].lower():
            result.append(post)
    if len(result) == 0:
        raise ValueError('такого пользователя нет')
    return result


def get_comments_by_post_id(post_id, path):
    """возвращает комментарии определенного поста."""
    result = []
    for comment in get_comments_all(path):
        if post_id in str(comment['post_id']):
            result.append(comment)
    if len(result) is None:
        raise ValueError('такого поста нет')
    return result


def search_for_posts(query, path):
    """возвращает список постов по ключевому слову"""
    result = []
    if len(query) > 0:
        for post in get_posts_all(path):
            if query.lower() in post['content'].lower():
                result.append(post)
    return result


def get_post_by_pk(pk, path):
    """get_post_by_pk(pk)"""
    result = []
    for post in get_posts_all(path):
        if pk in str(post['pk']):
            result.append(post)
    if len(result) == 0:
        raise ValueError('такого поста нет')
    return result


def add_post(post):
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
