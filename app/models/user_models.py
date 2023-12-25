from app import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password

def get_data():
    return Users.query.all()
def create_data(content):

    username = content["username"]
    password = content["password"]

    new_user = Users(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    # return new_user