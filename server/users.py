from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
users_store = []
static_id = 1

@app.route("/users", methods=['GET', 'POST'])
def users():
    global static_id

    if request.method == 'POST':
        user = {'id': static_id, 'username': request.form['username'], 'email': request.form['email']}
        users_store.append(user)
        static_id+=1
        return user
    else:
        return users_store

@app.route("/users/<userid>", methods=['GET', 'DELETE'])
def user(userid):
    c_user = None
    for user_stored in users_store:
        if user_stored['id'] == int(userid):
            c_user = user_stored
            break

    if request.method == 'DELETE':
        if c_user is None:
            return {'success': 0}
        
        users_store.remove(c_user)
        return {'success': 1}
    else:
        return c_user
        
if __name__ == "__main__":
   app.run(debug=True, port=5001)