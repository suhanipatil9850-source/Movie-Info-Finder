import os
import requests

API_KEY = os.getenv('OMDB_API_KEY', 'YOUR_API_KEY')


def fetch_movie_info(movie_title):
    if not movie_title:
        return {'error': 'Please enter a movie name.'}
    if not API_KEY or API_KEY == 'YOUR_API_KEY':
        return {'error': 'Set the OMDB_API_KEY environment variable to your OMDb API key.'}

    url = f'http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}'
    response = requests.get(url)
    if response.status_code != 200:
        return {'error': 'Unable to reach OMDb API.'}

    data = response.json()
    if data.get('Response') == 'True':
        return data
    return {'error': data.get('Error', 'Movie not found!')}


def print_movie_info(movie_title):
    data = fetch_movie_info(movie_title)
    if 'error' in data:
        print('❌', data['error'])
        return data

    print('\n🎬 Movie Information\n')
    print('Title:', data.get('Title'))
    print('Year:', data.get('Year'))
    print('Genre:', data.get('Genre'))
    print('IMDb Rating:', data.get('imdbRating'))
    print('Plot:', data.get('Plot'))
    return data


if __name__ == '__main__':
    movie = input('Enter movie name: ')
    print_movie_info(movie)
