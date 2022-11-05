# Functions for app
import json


# возвращает пост
def get_posts_all():
    try:
        with open('data/posts.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        print('Error')


# возвращает комментарии
def get_comments_all():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# возвращает посты определенного пользователя.
def get_posts_by_user(user_name):
    posts = get_posts_all()
    posts_user = []
    for post in posts:
        if post['poster_name'].lower() == user_name.lower():
            posts_user.append(post)
    if not posts_user:
        return ValueError
    return posts_user


# возвращает комментарии определенного поста
def get_comments_by_post_id(post_id):
    comments_id = []
    comments = get_comments_all()
    for comment in comments:
        if comment['post_id'] == post_id:
            comments_id.append(comment)
    return comments_id


# считает количество постов
def get_comments_count(pk):
    comments = get_comments_all()
    count = 0
    for comment in comments:
        if comment['post_id'] == pk:
            count += 1
    return count


# возвращает список постов по ключевому слову
def search_for_posts(query):
    posts = get_posts_all()
    posts_query = []
    for post in posts:
        if query.lower() in post['content'].lower():
            posts_query.append(post)
        elif not posts_query:
            return 'Не найдено постов'
    return posts_query


# возвращает один пост по его идентификатору.
def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if pk == post["pk"]:
            return post
