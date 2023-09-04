import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# Replace 'YOUR_API_KEY' with your actual TMDb API key.
api_key = '95aae346315fb162cb12a326ebce40b5'

# The base URL for TMDb API.
base_url = 'https://api.themoviedb.org/3'

# Function to search for a movie by title and update the GUI.
def search_movie():
    title = entry.get()
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
            first_movie = data['results'][0]
            result_text.set(f'Title: {first_movie["title"]}')
            release_date_text.set(f'Release Date: {first_movie["release_date"]}')
            overview_text.config(state=tk.NORMAL)
            overview_text.delete(1.0, tk.END)
            overview_text.insert(tk.END, f'Overview:\n{first_movie["overview"]}')
            overview_text.config(state=tk.DISABLED)
            genres_text.set(f'Genres: {first_movie["genre_ids"]}')
            popularity_text.set(f'Popularity: {first_movie["popularity"]}')
            vote_count_text.set(f'Vote Count: {first_movie["vote_count"]}')
            vote_average_text.set(f'Vote Average: {first_movie["vote_average"]}')
            
            # Display the movie ID
            movie_id_text.set(f'Movie ID: {first_movie["id"]}')
        else:
            messagebox.showinfo("No Results", "No movie found with that title.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f'Error: {e}')

# Create the main window
root = tk.Tk()
root.title("Movie Search App")

# Create and configure GUI elements
entry_label = tk.Label(root, text="Enter the title of the movie:")
entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_movie)
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
release_date_text = tk.StringVar()
release_date_label = tk.Label(root, textvariable=release_date_text)
overview_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, state=tk.DISABLED)
genres_text = tk.StringVar()
genres_label = tk.Label(root, textvariable=genres_text)
popularity_text = tk.StringVar()
popularity_label = tk.Label(root, textvariable=popularity_text)
vote_count_text = tk.StringVar()
vote_count_label = tk.Label(root, textvariable=vote_count_text)
vote_average_text = tk.StringVar()
vote_average_label = tk.Label(root, textvariable=vote_average_text)
movie_id_text = tk.StringVar()
movie_id_label = tk.Label(root, textvariable=movie_id_text)

# Place GUI elements on the window
entry_label.pack()
entry.pack()
search_button.pack()
result_label.pack()
release_date_label.pack()
overview_text.pack()
genres_label.pack()
popularity_label.pack()
vote_count_label.pack()
vote_average_label.pack()
movie_id_label.pack()

# Limit the maximum height of the window
root.maxsize(500, 600)

# Start the GUI main loop
root.mainloop()
