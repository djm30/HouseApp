from flask import Flask, render_template, url_for
from database.mongo_service import MongoService

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/<name>', methods=['GET'])
def hello(name=None):
    MongoService().insert_into_collection(
        "test_collection", "test", {"test": "testData"})
    return render_template("index.html", name=name)


@app.route('/test', methods=['GET'])
def test():
    return render_template("dash.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
