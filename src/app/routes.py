from werkzeug.utils import redirect
from app.database.models import User, Task, Post
from app import app
from flask import json, render_template, request, url_for, jsonify
from datetime import date

@app.route("/", methods=["GET"])
@app.route('/home', methods=['GET'])
def render_home():
    return render_template("index.html")




#TASK ROUTES

#RETURNS JSON OF ALL TASKS
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return Task.objects().to_json()

#RETURNS SINGLE TASK
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id = None):
    return Task.objects.get(id=id).to_json()

#ADDS NEW task
@app.route("/tasks/add", methods=['POST'])
def add_task():
    Task(task_name = request.get_json()["task_name"], currentUser = request.get_json()["current_user"]).save()
    return redirect(url_for("render_home"))

#UPDATE task
@app.route("/tasks/update/<id>", methods=["PATCH"])
def update_task(id = None):
    pass

#DELETE task
@app.route("/tasks/delete/<id>", methods=["DELETE"])
def delete_task(id = None):
    Task.objects.get(id = id).delete()
    return redirect(url_for("render_home"))




#POST ROUTES

#RETURNS JSON OF ALL POSTS
@app.route('/posts', methods=['GET'])
def get_posts():
    return Post.objects.to_json()

#RETURNS SINGLE POST
@app.route('/posts/<id>', methods=['GET'])
def get_post(id = None):
    return Post.objects.get(id=id).to_json()

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




#DEBT ROUTES

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

#USER ROUTES

#RETURNS JSON OF ALL USERS
@app.route('/users', methods=['GET'])
def get_users():
    return User.objects.to_json()

#RETURNS SINGLE USER
@app.route('/users/<id>', methods=['GET'])
def get_user(id = None):
    return User.objects.get(id=id).to_json()

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


# @app.route('/mongotest')
# def mongo_test():
#     dylan = User(name="Dylan")
#     task = Task(task_name="Bin", currentUser = dylan)
#     dylan.save()
#     task.save()
#     return "Mongo Test"



# @app.route('/', methods=['GET'])
# @app.route('/<name>', methods=['GET'])
# def hello(name=None):
#     MongoService().insert_into_collection(
#         "test_collection", "test", {"name": name})
#     return render_template("index.html", name=name)


# @app.route('/test', methods=['GET'])
# def hit_db():
#     return MongoService().get_from_collection(
#         "test_collection", "test"
#     )[0]["test"]


# @app.route('/note', methods=['POST'])
# def add_note():
#     payload = {
#         "title": request.get_json()["title"],
#         "content": request.get_json()["content"],
#         "date": str(date.today())
#     }
#     insert_payload(notes_collection, db_name, payload)


# @app.route('/rota/increment/<task>', methods=["POST"])
# def update_task(task):
#     response = jsonify()
#     try:
#         for task in MongoService().get_from_collection(rota_collection, db_name):
#             if (task["name"] == task):
#                 #new_person = task["person"] + 1
#                 #MongoService().update_into_collection(rota_collection, db_name, task, "person", new_person)
#                 response.status_code = 200
#     except Exception as e:
#         return e
#         response.status_code = 400
#     return response


# @app.route('/rota/new/<name>', methods=['POST'])
# def add_task(name):
#     payload = {
#         "task": name,
#         "person_id": request.get_json()["person_id"]
#     }
#     return insert_payload(rota_collection, db_name, payload)


# def insert_payload(rota_collection, db_name, payload):
#     response = jsonify()
#     try:
#         MongoService().insert_into_collection(rota_collection, db_name, payload)
#         response.status_code = 200
#     except:
#         response.status_code = 400

#     return response


# @app.route('/dash', methods=['GET'])
# def test():
#     return render_template("dash.html")
