import pytest
from utils import search_for_posts

path = '../data/posts.json'
keys_should_be = {'content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'}


def test_get_posts_by_user():
    post = search_for_posts('Квадратная', path)
    assert type(post) == list, 'возвращается не список'
    assert len(post) == 1, 'неправильная длина списка'
    assert set(post[0].keys()) == keys_should_be, 'неправильные ключи'
