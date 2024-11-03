# movie finder app
import requests

class MovieDescription:
    # constructor
    def __init__(self, api_key):
        self.api_key = api_key

    # method
    def searched_movie(self, title):
        try:
            # fetch movie data from the API
            url = f'http://www.omdbapi.com/?t={title}&apikey={self.api_key}'
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                if data.get('Response') == 'True':
                    # display movie information
                    print("******************************************")
                    print(f"Movie Title: {data.get('Title')}")
                    print(f"Movie Year: {data.get('Year')}")
                    print(f"Movie Rated: {data.get('Rated')}")
                    print(f"Movie Released: {data.get('Released')}")
                    print(f"Movie Runtime: {data.get('Runtime')}")
                    print(f"Movie Genre: {data.get('Genre')}")
                    print(f"Movie Director: {data.get('Director')}")
                    print(f"Movie Writer: {data.get('Writer')}")
                    print("******************************************")
                else:
                    print("******************************************")
                    print(f"No movies exist with this title: {title}")
                    print("******************************************")
            else:
                print("Error fetching data from the API.")

        except Exception as e:
            print(e)


api_key = '42527132'  # replace with your actual API key
# create object
movie = MovieDescription(api_key)

# while loop to run program continuously
while True:
    try:
        title = input("Enter movie title: ")
        print("Searching movie............")
        # call method
        movie.searched_movie(title)
        
        choice = input("Would you like to continue? (y/n): ").lower()
        if choice == 'y' or choice == 'yes':
            continue
        elif choice == 'n' or choice == 'no':
            print("******************************************")
            print("Thank you for using movie finder app..")
            print("******************************************")
            break
        else:
            print("******************************************")
            print("Invalid input, please try again!!")
            print("******************************************")
    except Exception as e:
        print(e)
