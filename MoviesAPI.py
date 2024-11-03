import requests


class CallingMovies:

    def __init__(self, api_key):
        self.api_key = api_key

    def search_movie(self, title):
        try:
            url = f"http://www.omdbapi.com/?t={title}&apikey={self.api_key}"
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                if data.get('Response') == 'True':
                    print('--------------------------')
                    print('Movie title:', data.get('Title'))
                    print('Movie year:', data.get('Year'))
                    print('Movie rated:', data.get('Rated'))
                    print('Movie director:', data.get('Director'))
                    print('Movie writer:', data.get('Writer'))
                    print('--------------------------')
                else:
                    print('--------------------------')
                    print('No movie with the title:', {title}, "exists........")
                    print('--------------------------')
        except Exception as e:
            print(f"An error occurred: {e}")


api_key = 'c061a146'
movie = CallingMovies(api_key)
while True:
    title = input("Enter the name of the movie: ")
    movie.search_movie(title)
    choice = input("Would you like to continue press: (y/n):").lower()
    if choice == 'y' or choice == 'yes':
        continue
    elif choice == 'n' or choice == 'no':
        print("---------------------------")
        print("Thank you for using movie info app :).......")
        print("---------------------------")
    else:
        print("---------------------------")
        print('Please enter a valid statement!!!!!')
        print("---------------------------")
