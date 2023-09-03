import unittest

from API_requests.simple_books_requests import SimpleBooksRequests


class TestGetBook(unittest.TestCase):
    """
    Testam ruta GET/book/bookID
    """

    def setUp(self) -> None:
        self.request_handler = SimpleBooksRequests()

    def test_get_book_by_valid_id(self):
        """
        Verificam:
        - status code este 200
        - id-ul obtinut in response este exact cel furnizat
        """
        book_id = 5
        response = self.request_handler.get_book_by_id(book_id=book_id)
        expected_status_code = 200
        expected_book_id = book_id
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_book_id, response.json()['id'])

    def test_get_book_by_invalid_id(self):
        """
        Verificam:
        - status code este 404
        - in response obtinel mesajul de eroare asteptat
        """
        book_id = 10
        response = self.request_handler.get_book_by_id(book_id=book_id)
        expected_status_code = 404
        expected_error_msg = f"No book with id {book_id}"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error_msg, response.json()['error'])