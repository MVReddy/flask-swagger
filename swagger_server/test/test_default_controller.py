# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_movie(self):
        """Test case for add_movie

        
        """
        movie = Movie()
        response = self.client.open(
            '/api/movies/{movie_id}'.format(movie_id='movie_id_example'),
            method='POST',
            data=json.dumps(movie),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_movies(self):
        """Test case for find_movies

        
        """
        query_string = [('tags', 'tags_example'),
                        ('limit', 56)]
        response = self.client.open(
            '/api/movies',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movie(self):
        """Test case for get_movie

        
        """
        response = self.client.open(
            '/api/movies/{movie_id}'.format(movie_id='movie_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
