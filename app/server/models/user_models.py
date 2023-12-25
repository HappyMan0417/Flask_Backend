from server import db

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

    return new_user
def update_data_by_id(userid, content):

    user = Users.query.get(userid)

    if not user:
        return None
    username = content["username"]
    password = content["password"]
    user.username = username
    user.password = password
    db.session.commit()
    return {"message": "User updated successfully", "user": content}, 200 
    
    # return new_user

def delete_data_by_id(userid):
    user_to_delete = Users.query.get(userid)

    if user_to_delete is None:
        return None  # return None if user not found

    db.session.delete(user_to_delete)
    db.session.commit()

    return {"message": "User deleted successfully"}, 200