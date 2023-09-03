import unittest

from API_requests.simple_books_requests import SimpleBooksRequests


class TestGetBooks(unittest.TestCase):
    """
    Testam ruta GET /books
    """

    def setUp(self):
        self.requests_handler = SimpleBooksRequests()

    def test_get_all_books_when_no_params_provided(self):
        """
        Verificam:
         - status code este 200
         - in response am obtinut exact 6 carti
        """
        response = self.requests_handler.get_all_books()
        expected_status_code = 200
        expected_books_number = 6
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_books_number, len(response.json()))

    def test_get_all_books_when_type_is_fiction(self):
        """
        Verificam:
        - status code este 200
        - in response am obtinut exact 4 carti
        - fiecare carte din response are type fiction
        """
        response = self.requests_handler.get_all_books(type="fiction")
        expected_status_code = 200
        expected_books_number = 4
        expected_books_type = "fiction"
        books_list = response.json()
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_books_number, len(books_list))
        for book in books_list:
            self.assertEqual(expected_books_type, book['type'])
            print(f'{book["id"]}')

    def test_get_all_books_when_type_is_nonfiction(self):
        """
        Verificam:
        - status code este 200
        - in response am obtinut exact 2 carti
        - fiecare carte din response are type non-fiction
        """
        response = self.requests_handler.get_all_books(type="non-fiction")
        expected_status_code = 200
        expected_books_number = 2
        expected_books_type = "non-fiction"
        books_list = response.json()
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_books_number, len(books_list))
        for book in books_list:
            self.assertEqual(expected_books_type, book['type'])
            print(f'{book["id"]}')

    def test_get_all_books_when_limit_is_between_1_6(self):
        """
        Verificam:
        - status code este 200
        - obtinem exact atatea carti cat am setat limit-ul
        """
        limit = 3
        response = self.requests_handler.get_all_books(limit=limit)
        expected_status_code = 200
        expected_books_number = limit
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_books_number, len(response.json()))

    def test_get_all_books_when_limit_is_between_7_20(self):
        """
        Verificam:
        - status code este 200
        - obtinem toata lista de carti disponibila
        """
        limit = 9
        response = self.requests_handler.get_all_books(limit=limit)
        expected_status_code = 200
        expected_books_number = 6
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_books_number, len(response.json()))

    def test_get_all_books_when_limit_is_negative_number(self):
        """
        Verificam:
        - status code este 400
        - obtinem eroarea asteptata
        """
        response = self.requests_handler.get_all_books(limit=-7)
        expected_status_code = 400
        expected_error_msg = "Invalid value for query parameter 'limit'. Must be greater than 0."
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error_msg, response.json()['error'])

    def test_get_all_books_when_limit_is_not_number(self):
        """
        Verificam:
        - status code este 200
        - obtinem toata lista de carti disponibila
        - atributele primei carti (id si titlu)
        """
        response = self.requests_handler.get_all_books(limit="z")
        expected_status_code = 200
        expected_books_number = 6
        expected_first_book_id = 1
        expected_first_book_title = "The Russian"
        books_list = response.json()
        first_book = books_list[0]
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_books_number, len(books_list))
        self.assertEqual(expected_first_book_id, first_book['id'])
        print(first_book['id'])
        self.assertEqual(expected_first_book_title, first_book['name'])
        print(first_book['name'])
