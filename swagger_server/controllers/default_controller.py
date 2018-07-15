import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server import util


def add_movie(movie_id, movie=None):  # noqa: E501
    """add_movie

    Add a new movie to the collection # noqa: E501

    :param movie_id: The movie&#39;s movie_id
    :type movie_id: str
    :param movie: The Movie JSON you want to post
    :type movie: dict | bytes

    :rtype: Movie
    """
    if connexion.request.is_json:
        movie = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return movie


def find_movies(tags=None, limit=None):  # noqa: E501
    """find_movies

    Returns all movies from the system # noqa: E501

    :param tags: Tags used to filter the result
    :type tags: List[str]
    :param limit: maximum number of results to return
    :type limit: int

    :rtype: List[Movie]
    """
    return 'do some magic!'


def get_movie(movie_id):  # noqa: E501
    """get_movie

    Returns a single movie by its movie_id # noqa: E501

    :param movie_id: The movie&#39;s movie_id
    :type movie_id: str

    :rtype: Movie
    """
    return 'do some magic!'
