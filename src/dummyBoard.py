from flask import Flask, redirect, url_for, request
from flask.templating import render_template
from jinja2.loaders import BaseLoader

#does something...
app = Flask(__name__)

dummy_turn_to_buy = [
    {
        "Item": "Tiolet Paper",
        "Person": "Person A"
    },
    {
        "Item": "Milk",
        "Person": "Person B"
    },
    {
        "Item": "Washing up Liquid",
        "Person": "Person C"
    },
    {
        "Item": "Gas",
        "Person": "Person D"
    },
]

@app.route("/")
def get_board():
    items = []
    people = []
    for row in dummy_turn_to_buy:
        items.append(row["Item"])
        people.append(row["Person"])
    turn_to_buy = [items,people]
    return render_template('board.html', turn_to_buy=turn_to_buy)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")