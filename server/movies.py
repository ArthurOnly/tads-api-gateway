from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
movies_store = [{'id': 1, 'title': 'Livro teste'}, {'id': 2, 'title': 'Livro teste 2'}]
static_id = 1

@app.route("/movies", methods=['GET', 'POST'])
def movies():
    global static_id

    if request.method == 'POST':
        movie = {'id': static_id, 'title': request.form['title']}
        movies_store.append(movie)
        static_id+=1
        return movie
    else:
        return movies_store

@app.route("/movies/<movieid>", methods=['GET', 'DELETE'])
def movie(movieid):
    c_movie = None
    for movie_stored in movies_store:
        if movie_stored['id'] == int(movieid):
            c_movie = movie_stored
            break

    if request.method == 'DELETE':
        if c_movie is None:
            return {'success': 0}
        
        movies_store.remove(c_movie)
        return {'success': 1}
    else:
        return c_movie

if __name__ == "__main__":
   app.run(debug=True, port=5002)