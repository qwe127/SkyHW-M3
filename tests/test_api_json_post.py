import pytest

from main import app

keys_should_be = {'content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'}


def test_app():
    response = app.test_client().get('api/posts/1', follow_redirects=True)
    assert response.status_code == 200
    assert type(response.json) == list, 'возвращается не список'
    assert set(response.json[0].keys()) == keys_should_be, 'неправильные ключи'
