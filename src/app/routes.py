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
    pass

#RETURNS SINGLE TASK
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id = None):
    pass

#ADDS NEW task
@app.route("/tasks/add", methods=['POST'])
def add_task():
    pass

#UPDATE task
@app.route("/tasks/update/<id>", methods=["PATCH"])
def update_task(id = None):
    pass

#DELETE task
@app.route("/tasks/delete/<id>", methods=["DELETE"])
def delete_task(id = None):
    pass


#POST ROUTES

#RETURNS JSON OF ALL POSTS
@app.route('/posts', methods=['GET'])
def get_posts():
    pass

#RETURNS SINGLE POST
@app.route('/posts/<id>', methods=['GET'])
def get_post(id = None):
    pass

#ADDS NEW POST
@app.route("/posts/add", methods=['POST'])
def add_post():
    pass

#UPDATE POST
@app.route("/posts/update/<id>", methods=["PATCH"])
def update_post(id = None):
    pass

#DELETE POST
@app.route("/posts/delete/<id>", methods=["DELETE"])
def delete_post(id = None):
    pass




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

#RETURNS JSON OF ALL userS
@app.route('/users', methods=['GET'])
def get_users():
    pass

#RETURNS SINGLE DEBT
@app.route('/users/<id>', methods=['GET'])
def get_user(id = None):
    pass

#ADDS NEW DEBT
@app.route("/users/add", methods=['POST'])
def add_user():
    pass

#UPDATE DEBT
@app.route("/users/update/<id>", methods=["PATCH"])
def update_user(id = None):
    pass

#DELETE DEBT
@app.route("/users/delete/<id>", methods=["DELETE"])
def delete_user(id = None):
    pass


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
