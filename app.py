import os
from flask import Flask, render_template, request, jsonify
from j import fetch_movie_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/movie')
def movie_info():
    title = request.args.get('title', '').strip()
    result = fetch_movie_info(title)
    if 'error' in result:
        return jsonify({'error': result['error']}), 400
    return jsonify({
        'title': result.get('Title'),
        'year': result.get('Year'),
        'genre': result.get('Genre'),
        'imdb_rating': result.get('imdbRating'),
        'plot': result.get('Plot'),
        'poster': result.get('Poster'),
        'type': result.get('Type'),
        'runtime': result.get('Runtime'),
        'director': result.get('Director'),
        'actors': result.get('Actors'),
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
