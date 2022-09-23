import pytest
from utils import get_posts_all

path = '../data/posts.json'


def test_get_posts_by_user():
    posts = get_posts_all(path)
    assert type(posts) == list, 'возвращается не список'
    assert len(posts) == 8, 'неправильная длина списка'
