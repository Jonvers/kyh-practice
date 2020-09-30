import requests


def main():
    movie_name = input("Vad vill du se för film?")
    movie = movie_req(name=movie_name)
    print(f"***Resultat från OMDB!***\n{movie['Title']} ({movie['Year']}) Regisserades av {movie['Director']} \n"
          f"Skådisar: {movie['Actors']} \nIMDB betyg: {movie['imdbRating']} \n"
          f"Awards: {movie['Awards']} \nLängd: {movie['Runtime']}")


def movie_req(name):
    r = requests.get("http://www.omdbapi.com/", params={"t": name, "apikey": "9f6d550c"})
    return r.json()


if __name__ == '__main__':
    main()
