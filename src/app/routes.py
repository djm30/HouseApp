from logging import error
from werkzeug.utils import redirect
from app.database.models import User, Task, Post
from app.database.testdata import save_data
from app import app
from flask import json, render_template, request, url_for, jsonify, flash
from datetime import date
from app.forms.AddTask import TaskForm
from flask_wtf import FlaskForm
import sys

@app.route("/", methods=["GET", "POST"])
@app.route('/home', methods=['GET', "POST"])
def render_home():
    return render_template("index.html", tasks = get_tasks()["Tasks"], users = get_users()["Users"])


#SELF EXPLANATORY, ADDS TEST DATA TO DATABASE
@app.route("/createtestdata")
def create_data():
    save_data()
    return "DATA SAVED"


#TASK ROUTES

#RETURNS JSON OF ALL TASKS
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return {"Tasks": Task.objects}


#ADDS NEW task
@app.route("/tasks/add", methods=['POST'])
def add_task():
    print("FUCK FUCK",file=sys.stderr)
    Task(task_name = request.get_json()["task_name"], current_user = request.get_json()["current_user"]).save()
    return {"status" : "success"}

#RETURNS SINGLE TASK
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id = None):
    return {"Task" :Task.objects.get(id=id)}

#UPDATE task
@app.route("/tasks/update/<id>", methods=["PATCH"])
def update_task(id = None):
    pass

#UPDATE users associated with tasks
@app.route("/tasks/update", methods=["PATCH"])
def update_task_user():
    max_length = len(User.objects.all())
    data = request.get_json()["selected"]
    try:
        for task in data:
            task_id, user_id  = tuple(task.split("_"))
            user_id = int(user_id)
            if user_id+1 > max_length:
                user_id = 1
            else: user_id+=1
            task = Task.objects.get(id = task_id)
            task.current_user = User.objects.get(_id = user_id)
            task.save()
        return "Info updated successfully!"
    except error as e:
        return "Error updating task"

#DELETE task
@app.route("/tasks/delete/<id>", methods=["DELETE"])
def delete_task(id = None):
    Task.objects.get(id = id).delete()
    return redirect(url_for("render_home"))




#POST ROUTES
#region

#RETURNS JSON OF ALL POSTS
@app.route('/posts', methods=['GET'])
def get_posts():
    return {"Posts" : Post.objects}

#RETURNS SINGLE POST
@app.route('/posts/<id>', methods=['GET'])
def get_post(id = None):
    return {"Post" : Post.objects.get(id=id)}

#ADDS NEW POST
@app.route("/posts/add", methods=['POST'])
def add_post():
    Post(
        post_title = request.get_json()["post_name"], 
        post_content = request.get_json()["post_content"], 
        post_author = request.get_json()["post_author"]).save()
    return redirect(url_for("render_home"))

#UPDATE POST
@app.route("/posts/update/<id>", methods=["PATCH"])
def update_post(id = None):
    pass

#DELETE POST
@app.route("/posts/delete/<id>", methods=["DELETE"])
def delete_post(id = None):
    Post.objects.get(id = id).delete()
    return redirect(url_for("render_home"))
#endregion



#DEBT ROUTES
#region
#RETURNS JSON OF ALL DEBTS
@app.route('/debts', methods=['GET'])
def get_debts():
    pass

#RETURNS SINGLE DEBT
@app.route('/debts/<id>', methods=['GET'])
def get_debt(id = None):
    pass

#ADDS NEW DEBT
@app.route("/debts/add", methods=['POST'])
def add_debt():
    pass

#UPDATE DEBT
@app.route("/debts/update/<id>", methods=["PATCH"])
def update_debt(id = None):
    pass

#DELETE DEBT
@app.route("/debts/delete/<id>", methods=["DELETE"])
def delete_debt(id = None):
    pass
#endregion

#USER ROUTES
#region
#RETURNS JSON OF ALL USERS
@app.route('/users', methods=['GET'])
def get_users():
    return {"Users" : User.objects}

#RETURNS SINGLE USER
@app.route('/users/<id>', methods=['GET'])
def get_user(id = None):
    return {"User" : User.objects.get(id=id)}

#ADDS NEW USER
@app.route("/users/add", methods=['POST'])
def add_user():
    User(name = request.get_json()["name"]).save()
    return redirect(url_for("render_home"))


#UPDATE USER
@app.route("/users/update/<id>", methods=["PATCH"])
def update_user(id = None):
    pass

#DELETE USER
@app.route("/users/delete/<id>", methods=["DELETE"])
def delete_user(id = None):
    User.objects.get(id = id).delete()
    return redirect(url_for("render_home"))
#endregion

