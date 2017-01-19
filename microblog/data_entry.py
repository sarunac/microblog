'''
Mock data entry with sqlAlchemy
'''
from app import db, models
import datetime

def create_users():
    usrs= [
    {'name':'sarun','email':'sarun@yahoo.com'},
    {'name':'aishwarya','email':'aishwarya@yahoo.com'} ]

    for usr in usrs:
       u = models.User(name=usr['name'], email=usr['email'])
       db.session.add(u)

    db.session.commit()

    users = models.User.query.all()
    print users
    for usr in users:
        print(usr.id,usr.name)


def write_post(user_id):
    usr = models.User.query.get(user_id)
    post = models.Post(body='my first post with sqlAlchemy', timestamp=datetime.datetime.utcnow(), author=usr)
    db.session.add(post)
    db.session.commit()


def get_post(user_id):
    usr = models.User.query.get(user_id)
    print 'for User ',usr
    posts = usr.posts.all()
    print 'Posts: ',posts

def clear_all():
    users = models.User.query.all()
    for u in users:
        db.session.delete(u)

    posts = models.Post.query.all()
    for p in posts:
        db.session.delete(p)
    db.session.commit()

print 'Clearing database'
clear_all()
print 'creating users'
create_users()
print 'Writing posts for user 1'
write_post(1)
print 'Extracting posts for user 1'
get_post(1)
print 'Extracting posts for user 2'
get_post(2)
print 'Clearing database'
clear_all()