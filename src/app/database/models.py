import mongoengine as me
from datetime import datetime

class User(me.Document):
    _id = me.SequenceField(primary_key=True)
    name = me.StringField(required=True, unique=True)

class Task(me.Document):
    task_name = me.StringField(required=True, unique=True)
    current_user = me.ReferenceField(User, required=True)

class Post(me.Document):
    post_title = me.StringField(required=True)
    post_content = me.StringField(required=True)
    post_author = me.ReferenceField(User, required=True)
    post_date = me.DateField(required=True, default=datetime.now)