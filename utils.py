# Functions for app
import json


def get_posts_all():
    """Возвращает пост"""
    try:
        with open('data/posts.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        print('Error')


def get_comments_all():
    """Возвращает комментарии"""
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    posts = get_posts_all()
    posts_user = []
    for post in posts:
        if post['poster_name'].lower() == user_name.lower():
            posts_user.append(post)
    if not posts_user:
        return ValueError
    return posts_user


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    comments_id = []
    comments = get_comments_all()
    for comment in comments:
        if comment['post_id'] == post_id:
            comments_id.append(comment)
    return comments_id


def get_comments_count(pk):
    """Считает количество постов"""
    comments = get_comments_all()
    count = 0
    for comment in comments:
        if comment['post_id'] == pk:
            count += 1
    return count


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    posts_query = []
    for post in posts:
        if query.lower() in post['content'].lower():
            posts_query.append(post)
        elif not posts_query:
            return 'Не найдено постов'
    return posts_query


def get_post_by_pk(pk):
    """Возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    for post in posts:
        if pk == post["pk"]:
            return post
