def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])


def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])


def has_director_made_genre(movies, director, genre):
    return any([movie for movie in movies if movie.director == director if genre in movie.genres])


def is_prime(ns):
    return all(ns % k != 0 for k in range(2, ns)) and ns >= 2


def is_increasing(ns):
    return all(x <= y for x, y in zip(ns, ns[1:]))


def count_matching(xs, ys):
    return sum(x == y for x, y in zip(xs, ys))


def weighted_sum(ns, weights):
    return sum(n * w for n, w in zip(ns, weights))


def alternating_caps(string):
    chars = [char.upper() if index % 2 == 0 else char.lower()
             for index, char in enumerate(string)]
    return "".join(chars)


def find_repeated_words(sentence):
    import re
    words = [word.lower() for word in re.findall('[a-zA-Z]+', sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}
