from app import db
from models.user_model import User
from models.post_model import Post
import random


def seedUser(db):
    users = [
        {'email': 'user1@gmail.com', 'username': 'user1'},
        {'email': 'user2@gmail.com', 'username': 'user2'},
        {'email': 'user3@gmail.com', 'username': 'user3'},
        {'email': 'user4@gmail.com', 'username': 'user4'},
    ]

    for u in users:
        user = User(username=u['username'], email=u['email'])
        db.session.add(user)
    db.session.commit()


def seedPost(db, userIds):
    posts = [
        {'title': 'The title post 1', 'content': 'The content post 1'},
        {'title': 'The title post 2', 'content': 'The content post 2'},
        {'title': 'The title post 3', 'content': 'The content post 3'},
        {'title': 'The title post 4', 'content': 'The content post 4'},
        {'title': 'The title post 5', 'content': 'The content post 5'},
    ]

    for p in posts:
        userId = random.choice(userIds)
        post = Post(title=p['title'], content=p['content'], author_id=userId)
        db.session.add(post)
    db.session.commit()


if __name__ == "__main__":
    db.create_all()
    seedUser(db)
    seedPost(db, [1, 2, 3])
