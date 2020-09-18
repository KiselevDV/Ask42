from my_app.app import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<Message {self.id}'
