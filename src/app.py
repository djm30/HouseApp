from logging import exception
from flask import Flask, json, render_template, request, url_for, jsonify
from flask.wrappers import Response
from database.mongo_service import MongoService
from datetime import date

app = Flask(__name__)

db_name = "tates2"
notes_collection = "notes"
rota_collection = "rota"

@app.route('/', methods=['GET'])
@app.route('/<name>', methods=['GET'])
def hello(name=None):
    MongoService().insert_into_collection(
        "test_collection", "test", {"name": name})
    return render_template("index.html", name=name)

@app.route('/test', methods=['GET'])
def hit_db():
    return MongoService().get_from_collection(
        "test_collection", "test"
    )[0]["test"]

@app.route('/note', methods=['POST'])
def add_note():
    payload = {
        "title": request.get_json()["title"],
        "content": request.get_json()["content"],
        "date": str(date.today())
    }
    insert_payload(notes_collection, db_name, payload)

@app.route('/rota/increment/<task>', methods=["POST"])
def update_task(task):
    response = jsonify()
    try:        
        for task in MongoService().get_from_collection(rota_collection, db_name):
            if (task["name"] == task):
                #new_person = task["person"] + 1
                #MongoService().update_into_collection(rota_collection, db_name, task, "person", new_person)
                response.status_code=200
    except Exception as e:
        return e
        response.status_code=400
    return response

@app.route('/rota/new/<name>', methods=['POST'])
def add_task(name):
    payload = {
            "task": name,
            "person_id": request.get_json()["person_id"]
        }
    return insert_payload(rota_collection, db_name, payload)


def insert_payload(rota_collection, db_name, payload):
    response = jsonify()
    try:
        MongoService().insert_into_collection(rota_collection, db_name, payload) 
        response.status_code = 200 
    except:
        response.status_code = 400
        
    return response


@app.route('/test', methods=['GET'])
def test():
    return render_template("dash.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
