import unittest

from API_requests.simple_books_requests import SimpleBooksRequests


class TestGetOrder(unittest.TestCase):
    """
    Testam ruta GET /orders/{orderId}
    """

    def setUp(self) -> None:
        self.request_handler = SimpleBooksRequests()

    def test_get_order_with_valid_id(self):
        """
        Verificam:
        - status code este 200
        - Id-ul comenzii interogate este egal cu Id-ul comenzii plasate
        """
        place_order = self.request_handler.submit_order(5, 'Laurentia')
        order_id = place_order.json()['orderId']
        response = self.request_handler.get_order_by_id(order_id=order_id)
        expected_status_code = 200
        expected_order_id = order_id
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_order_id, response.json()['id'])

    def test_get_order_with_invalid_id(self):
        """
        Verificam:
        - status code este 404
        - mesajul de eroare este cel asteptat
        """
        order_id = 'aaaaaaaaaaaaaaaa'
        response = self.request_handler.get_order_by_id(order_id=order_id)
        expected_status_code = 404
        expected_error_msg = f'No order with id {order_id}.'
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error_msg, response.json()['error'])