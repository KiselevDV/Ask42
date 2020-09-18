from flask import render_template, request, url_for, json
from my_app.app import app, db
from my_app.models import Message


@app.route('/', methods=['GET'])
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']

    message = Message(text=text)

    try:
        db.session.add(message)
        db.session.commit()
        db.session.close()
        return json.dumps(text)
    except:
        return 'An error occurred while adding an article'
