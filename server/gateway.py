from flask import Flask
from flask import request
from flask import request
import httpx
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USERS_API_URL = 'http://localhost:5001/'
MOVIES_API_URL = 'http://localhost:5002/'

@app.route("/users", methods=['GET', 'POST'])
def index_users():
    if request.method == 'GET':
        return httpx.get(f"{USERS_API_URL}/users").text
    else:
        return httpx.post(f"{USERS_API_URL}/users", data=dict(request.form)).text

@app.route("/movies", methods=['GET'])
def index_movies():
    return httpx.get(f"{MOVIES_API_URL}/movies").text

if __name__ == "__main__":
   app.run(debug=True, port=5000)