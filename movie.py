import requests

# Replace 'YOUR_API_KEY' with your actual TMDb API key.
api_key = '95aae346315fb162cb12a326ebce40b5'

# The base URL for TMDb API.
base_url = 'https://api.themoviedb.org/3'

# Function to search for a movie by title.
def search_movie_by_title(title):
    endpoint = '/search/movie'
    params = {
        'api_key': api_key,
        'query': title
    }

    try:
        response = requests.get(f'{base_url}{endpoint}', params=params)
        response.raise_for_status()

        data = response.json()

        if data['results']:
            # Display information about the first matching movie.
            first_movie = data['results'][0]
            print(f'Title: {first_movie["title"]}')
            print(f'Release Date: {first_movie["release_date"]}')
            print(f'Overview: {first_movie["overview"]}')
        else:
            print('No movie found with that title.')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

# Input the movie title you want to search for.
movie_title = input('Enter the title of the movie: ')

# Call the search function.
search_movie_by_title(movie_title)

