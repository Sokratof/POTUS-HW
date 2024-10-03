import requests
from flask import Flask
from models import User
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://potus:potus@db:5432/webapp_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


def create():
    db.create_all()


@app.route('/')
def fetch():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            user = User(name=user['name'], username=user['username'], email=user['email'])
            db.session.add(user)
            db.session.commit()
            return {"message": "Users added successfully"}
    else:
        return {"error": f"Failed to fetch users. Status code: {response.status_code}"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
