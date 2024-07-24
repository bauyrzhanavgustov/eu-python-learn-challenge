from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        filtered_movies = filter(
            lambda movie: len(movie['country'].split(',')) >= 2 and movie.get('rating_kinopoisk') and movie[
                'rating_kinopoisk'].strip() != '' and float(movie['rating_kinopoisk']) > 0,
            list_of_movies
        )

        ratings = []
        for movie in filtered_movies:
            try:
                rating = float(movie['rating_kinopoisk'])
                ratings.append(rating)
            except ValueError:
                continue


        if not ratings:
            return 0.0

        average_rating = sum(ratings) / len(ratings)

        return average_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        filtered_movies = filter(
            lambda movie: movie.get('rating_kinopoisk') and movie['rating_kinopoisk'].strip() != '' and float(
                movie['rating_kinopoisk']) >= rating,
            list_of_movies
        )

        counts = map(lambda movie: movie['name'].lower().count('и'), filtered_movies)

        total_count = sum(list(counts))

        return total_count
