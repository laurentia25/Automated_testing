import unittest

from API_requests.simple_books_requests import SimpleBooksRequests


class TestSubmitOrder(unittest.TestCase):
    """
    Testam ruta POST /orders
    """

    def setUp(self) -> None:
        self.request_handler = SimpleBooksRequests()

    def test_order_an_available_book(self):
        """
        Verificam:
        - status code este 201
        - status-ul comenzii create este "true"
        """
        pass

    def test_order_unavailable_book(self):
        """
        Verificam:
        - status code este 404
        - mesajul de eroare este cel asteptat
        """
        pass

    def test_order_book_which_is_not_in_db(self):
        """
        Verificam:
        - status code este 400
        - mesajul de eroare este cel asteptat
        """
        pass