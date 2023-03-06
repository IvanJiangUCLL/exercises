def titles(movies):
    return [movie.title for movie in movies]


def titles_and_years(movies):
    return [(movie.title, movie.year) for movie in movies]


def titles_and_actor_counts(movies):
    return [(movie.title, len(movie.actors)) for movie in movies]


def longest_runtime(movies):
    return max([movie.runtime for movie in movies])