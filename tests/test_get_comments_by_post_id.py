import pytest
from utils import get_comments_by_post_id

path = '../data/comments.json'
keys_should_be = {'comment', 'commenter_name', 'pk', 'pk', 'post_id'}


def test_get_posts_by_user():
    post = get_comments_by_post_id('1', path)
    assert type(post) == list, 'возвращается не список'
    assert len(post) == 4, 'неправильная длина списка'
    assert set(post[0].keys()) == keys_should_be, 'неправильные ключи'
